
import stripe, traceback, simplejson, base64, hashlib, sys

from twisted.python.filepath import FilePath

from lae_util.servers import append_record

from lae_site.handlers.web import env
from lae_util.flapp import FlappCommand

from lae_site.handlers.main import HandlerBase

SUBSCRIPTIONS_FILE      = 'subscriptions.csv'
SERVICE_CONFIRMED_FILE  = 'service_confirmed.csv'
SIGNUP_FURL_FILE        = 'signup.furl'

flappcommand = None

def start(basefp):
    global flappcommand

    signup_furl_fp = basefp.child('secret_config').child(SIGNUP_FURL_FILE)
    flappcommand = FlappCommand(signup_furl_fp.path)
    return flappcommand.start()

class SubmitSubscriptionHandler(HandlerBase):

    def __init__(self, basefp):
        HandlerBase.__init__(self, out=None)
        self._logger_helper(__name__)
        self.basefp = basefp

    def render(self, request):
        #Parse request, info from stripe and subscriber
        stripe_authorization_token = self.get_arg(request, 'stripeToken')
        email_from_form = self.get_arg(request, 'email')
        stripefp = FilePath(self.basefp.path).child('secret_config').child('stripeapikey')
        assert (('leastauthority.com' not in stripefp.path) or ('_trial_temp' in stripefp.path)), "secrets must not be in production code repo"
        stripe_api_key = stripefp.getContent().strip()

        #invoke cc-charge by requesting subscription to recurring-payment plan
        try:
            customer = stripe.Customer.create(api_key=stripe_api_key, card=stripe_authorization_token, plan='S4', email=email_from_form)
        except stripe.CardError, e:
            print >>self.out, "Got an exception from the stripe.Customer.create call:"
            print >>self.out, dir(e)
            print >>self.out, repr(e)
            tmpl = env.get_template('subscription_signup.html')
            return tmpl.render({"errorblock": e.message}).encode('utf-8', 'replace')

        #log that a new subscription has been created (at stripe)
        leastauthority_subscription_id = base64.b32encode(hashlib.sha1(customer.subscription.id))
        subscriptions_fp = self.basefp.child(SUBSCRIPTIONS_FILE)
        append_record(subscriptions_fp, leastauthority_subscription_id)       

        def when_done():
            try:
                service_confirmed_fp = self.basefp.child(SERVICE_CONFIRMED_FILE)
                append_record(service_confirmed_fp, leastauthority_subscription_id)
            except Exception:
                # The request really did succeed, we just failed to record that it did. Log the error locally.
                traceback.print_exc(100, sys.stderr)
        def when_failed():
            try:
                pass  #XXX
            except Exception:
                traceback.print_exc(100, sys.stderr)
        try:        
            customer_pgpinfo = customer_pgpinfo = self.get_arg(request, 'pgp_pubkey')
            stdin = simplejson.dumps((customer.email,
                                      customer_pgpinfo,
                                      customer.id,
                                      customer.subscription.id,
                                      customer.subscription.plan.name),
                                     ensure_ascii=True
                                     )

            flappcommand.run(stdin, self.out)
        except Exception:
            traceback.print_exc(100, self.out)
            when_failed()

        # http://twistedmatrix.com/documents/current/web/howto/web-in-60/asynchronous.html
        tmpl = env.get_template('payment_verified.html')
        return tmpl.render({"productfullname":"Simple Secure Storage Service", "productname":"S4"}).encode('utf-8')
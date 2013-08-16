﻿Open Letter to Phil Zimmermann and Jon Callas of Silent Circle, On The Closure of the “Silent Mail” Service
####################################################################################################################

:date: 2013-08-16 9:00
:tags: silent circle, prism
:category: Letters
:slug: open_letter_silent_circle
:author: Zooko Wilcox-O'Hearn
:summary: This open letter is in response to the recent shutdown of Lavabit and the ensuing shutdown of Silent Circle's “Silent Mail” product.

This open letter is in response to the `recent shutdown of Lavabit`_ , the ensuing `shutdown of Silent Circle's “Silent Mail” product`_, `Jon Callas's posts about the topic on G+`_, and `Phil Zimmermann's interview in Forbes`_. Also, of course, all of this is unfolding in the context of the `2013 Mass Surveillance Scandal`_.

.. _recent shutdown of Lavabit: http://boingboing.net/2013/08/08/lavabit-email-service-snowden.html

.. _shutdown of Silent Circle's “Silent Mail” product: http://silentcircle.wordpress.com/2013/08/09/to-our-customers/

.. _Jon Callas's posts about the topic on G+: https://plus.google.com/112961607570158342254/posts/9uySMokvg7k

.. _Phil Zimmermann's interview in Forbes: http://www.forbes.com/sites/parmyolson/2013/08/09/e-mails-big-privacy-problem-qa-with-silent-circle-co-founder-phil-zimmermann/

.. _2013 Mass Surveillance Scandal: https://en.wikipedia.org/wiki/2013_mass_surveillance_scandal


Dear Phil and Jon: Hello there! It is good to have a chance to chat with you in public.

Please accept the following in the spirit of constructive criticism in which it is intended.

For those readers who don't know, I've known you both, personally and professionally, for decades. You've each written texts that I've learned from, inspired me to follow your example, we've worked together successfully, and you've mentored me. I have great respect for your technical abilities, your integrity, and your general reasonableness. Thank you for the all of that and for holding fast to your principles today, when we need it more than ever.

Now:

Your job is not yet done. Your customers are currently vulnerable to having all of their communications secretly monitored.

I just subscribed to the service at https://SilentCircle.com, and after I paid $120 for one year of service, it directed me to install the Silent Text app from Silent Circle on my android phone, which I did. Now, when I use that Silent Circle app to send text messages to other Silent Circle customers, I have no way of verifying whether it is really encrypting my message on my own phone, and if it is really keeping the encryption key only for me, or if it is leaking the contents of my messages or my encryption keys to you or to others.

If some attacker, for example the U.S. Federal Government — or to pick a different example the Zetas Mexican drug cartel — were to coerce Silent Circle into cooperating with them, then that attacker would simply require Silent Circle to distribute an update to the app, containing a backdoor.

There is no way for me to verify that any given version of Silent Text, including the one that I just installed, is correctly generating strong encryption keys and is protecting those keys instead of leaking them.

Therefore, how are your current products any safer for your users that the canceled Silent Mail product was? The only attacker against whom your canceled Silent Mail product was vulnerable but against whom your current products are safe is an attacker who would require you to backdoor your server software but who wouldn't require you to backdoor your client software.

Does that constraint apply to the U.S. Federal Government entities who are responsible for PRISM, for the shut-down of Lavabit, and so much else? No, that constraint does not apply to them. This was demonstrated in the Hushmail case in which the U.S. DEA asked Hushmail (a Canadian company) to turn over the plaintext of the email of one of its customers. Hushmail complied, shipping a set of CDs to the DEA containing the customer's messages.

The President of Hushmail `emphasized`_ in interviews with journalists at the time that Hushmail would be able to comply with such orders regardless of whether the customer used Hushmail's “client-to-server” (SSL) encryption or its “end-to-end” (Java applet) encryption.

.. _emphasized: http://www.wired.com/threatlevel/2007/11/hushmail-to-war/

Phil had been Chief Cryptographer of Hushmail years earlier, and was still a member of the Advisory Board of Hushmail at the time of that case. He commented about the case at that time, and he also `stated`_, correctly, that the Hushmail model of *unverified* end-to-end encryption was vulnerable to government coercion. That's the same model that Silent Circle uses today.

.. _stated: http://www.wired.com/threatlevel/2007/11/pgp-creator-def/

You have just taken the courageous act of publicly shutting down the Silent Mail product, and publicly stating your reasons for doing so. This, then, is your opportunity to make your stance consistent by informing your customers of the similar dangers posed by the software distribution practices currently used by Silent Circle (along with most of the rest of the industry).

I don't know the perfect solution to the problem of the *unverifiability* of today's software. But being frank about the current approach and the vulnerability that it imposes on users is the first step. People will listen to you about this, now. Let's start talking about it and we can start finding solutions.

Also, warn your users. Don't tell them the untruth that it is impossible for you to eavesdrop on their communications even if you try (as your company seems to be on the borderline of doing in public statements like these: [ `¹`_, `²`_]).

.. _¹: http://www.forbes.com/sites/parmyolson/2013/07/15/corporate-customers-flock-to-anti-snooping-app-silent-circle/
.. _²: http://techcrunch.com/2013/08/08/silent-circle-preemptively-shuts-down-encrypted-email-service-to-prevent-nsa-spying/

We're trying an approach to this problem, here at `LeastAuthority.com`_, of “*verifiable* end-to-end security”. For our data backup and storage service, all of the software is Free and Open Source, and it is distributed through channels which are out of our direct control, such as Debian and Ubuntu. Of course this approach is not perfectly secure — it doesn't guarantee that a state-level actor cannot backdoor our customers. But it does guarantee that *we* cannot backdoor our customers.

This currently imposes inconvenience on our customers, and I'm not saying it is the perfect solution, but it shows that there is more than one way to go at this problem. 

Thank you for your attention to these important matter, and your leadership in speaking out about them.

(By the way, `LeastAuthority.com`_ is not a competitor to Silent Circle. We don't offer voice, text, video, or email services, like Silent Circle does/did. What we offer is simply secure offsite *backup*, and a secure cloud storage API that people use to build other services.)

Regards,

Zooko Wilcox-O'Hearn

.. _LeastAuthority.com: https://LeastAuthority.com


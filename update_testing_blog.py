"""This script:
(1) updates a testing blog instance.
"""

import sys, subprocess

from lae_automation.server import update_blog

branch_check_command = ['/usr/bin/git', '--git-dir', '../secret_config/.git', 'branch', '--list', 'testing']
current_branch = subprocess.check_output(branch_check_command).strip()
if current_branch != "* testing":
    print "The testing branch of the secret_config repo must be checked out to run this script."
    sys.exit(1)

admin_keypair_name = "ec2sshadmin"
admin_privkey_path = "../secret_config/ec2sshadmin.pem"

blog_repo_path = "../blog_source/.git"
blog_repo_HEAD_command = ['/usr/bin/git', '--git-dir', blog_repo_path, 'rev-parse', 'HEAD']
blog_commit_ref = subprocess.check_output(blog_repo_HEAD_command).strip()
print blog_commit_ref

update_blog("107.21.225.70", blog_repo_path, blog_commit_ref, admin_privkey_path)

from __future__ import with_statement
from fabric.api import *

prod_host = 'example.com'

env.hosts = [prod_host]

def deploy(site_path="site_path/"):
   with cd('../../var/sites/%s' % site_path):
       sudo('hg pull -u')
       with cd('scripts/'):
           sudo('./db-restore ../backup/sql/*.sql.gz')

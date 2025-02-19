#!/usr/bin/env python
from os.path import join, realpath

import traceback
from src import config
from src.mysql import connector
from src.mysql.connector import errorcode

import sys
from site import addsitedir
addsitedir(join(realpath(__file__), 'src', 'mysql'))

with open(config.config_file) as f:
    conf = dict(l.strip().split('=', 1) for l in f.readlines() if l.strip() and l.strip()[0] != '#')
db_login = conf['db_login']
db_passw = conf['db_password']
db_port = conf['db_port']
db_server = conf['db_server']

db_name = 'orthomcl'

print 'server:', db_server
print 'port:', db_port
print 'login:', db_login
print 'password:', db_passw
print 'database:', db_name

try:
    cnx = connector.connect(
        user=db_login,
        password=db_passw,
        host=db_server,
        port=db_port,
        database=db_name,
        buffered=True)
except:
    print 'Exception', traceback.print_exc(limit=0)
else:
    print 'Connected'

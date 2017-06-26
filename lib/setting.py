# -*- coding: utf-8 -*-
sql_conf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'mg131415',
    'db': 'MG001',
    'charset': 'utf8'
    }

try:
    from lib.setting_env import *
except ImportError:
    pass
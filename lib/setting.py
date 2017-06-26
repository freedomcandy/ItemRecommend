# -*- coding: utf-8 -*-
sql_conf = {
    'host': '172.16.12.50',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'MG001',
    'charset': 'utf8'
    }

try:
    from lib.setting_env import *
except ImportError:
    pass
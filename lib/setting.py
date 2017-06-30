# -*- coding: utf-8 -*-

'''mysql配置文件'''
SQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'mg131415',
    'db': 'MG001',
    'charset': 'utf8'
    }

'''服务监听窗口'''
PORT = 8888

'''自动重载服务器代码'''
AUTO_LOAD = True

try:
    from lib.setting_env import *
except ImportError:
    pass
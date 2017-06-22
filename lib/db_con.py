# -*- coding: utf-8 -*-
from setting import sql_conf
from tornado_mysql import pools

pools.DEBUG = True

'''实例化一个'''
MySQL = pools.Pool(sql_conf)

if __name__ == '__main__':
    from tornado import ioloop
    ioloop.IOLoop.current()
    print(MySQL._opened_conns)
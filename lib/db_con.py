# -*- coding: utf-8 -*-
from lib.setting import sql_conf
from tornado_mysql import pools

pools.DEBUG = True

'''实例化一个'''
MySQL = pools.Pool(sql_conf)

async def Execute(*arg, **kwargs):
    results_set = await MySQL.execute(*arg, **kwargs)
    return [result for result in results_set.fetchall()]

if __name__ == '__main__':
    from tornado import ioloop
    async def connect_test():
        result = await MySQL.execute('select * from user limit 1;')
        for result in result.fetchall():
            print(result)
    ioloop.IOLoop.current().run_sync(connect_test)
    print(MySQL._opened_conns)
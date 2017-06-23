# -*- coding: utf-8 -*-
from model.user import User

def myMLFunc(this_in_put):
    '''这是极其学习的算法'''
    this_out_put = 0
    '''输入this_in_put，输出this_out_put'''
    return this_out_put

async def test_main(user_id):
    '''这个函数展示了如何获取对应user_id的最后20次输出，
    并调用了机器学习算法'''
    user_obj = await User(user_id).initCategory()
    return myMLFunc(user_obj.last_cat)

if __name__ == '__main__':
    '''通过异步的方法执行逻辑'''
    from tornado import ioloop
    ioloop.IOLoop.current().run_sync(lambda: test_main(529))
# -*- coding: utf-8 -*-
from model.user import User
import ml.multi_percept as mlp

def myMLFunc(this_in_put):
    '''这是极其学习的算法'''
    this_out_put = 0
    '''输入this_in_put，输出this_out_put'''
    return this_out_put

async def test_main(user_id):
    '''这个函数展示了如何获取对应user_id的最后20次输出，
    并调用了机器学习算法'''
    user_obj = await User(user_id).initCategory()
    second_info = await user_obj.mlSecondCategory()
    df_obj = user_obj.mlThirdCategory()
    print(df_obj)
#     return myMLFunc(user_obj.last_view)
    return mlp.MultiLayerPerceptron().getTargetItemCluster(second_info)
#     return mlp.MultiLayerPerceptron().processMLPClassifier(user_obj.user_id, df_obj)


if __name__ == '__main__':
    '''通过异步的方法执行逻辑'''
    from tornado import ioloop
    ioloop.IOLoop.current().run_sync(lambda: test_main(673))
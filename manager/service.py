# -*- coding: utf-8 -*-
from lib.lru import LRUCache
from model.user import User

class mainService(object):
    def __init__(self):
        '''缓存暂定为全部用户的1/3'''
        self.user_cache = LRUCache(300)
        
    def getUser(self, user_id):
        user_id = int(user_id)
        if not user_id in self.user_cahce:
            self.user_cahce[user_id] = User(user_id)
        return self.user_cahce.get(user_id, None)
    
try:
    Service
except NameError:
    Service = mainService()
        
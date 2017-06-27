# -*- coding: utf-8 -*-
from lib.lru import LRUCache
from model.user import User

class cacheData(object):
    def __init__(self):
        self.item = LRUCache(500)
        self.user = LRUCache(200)
        
    def getUserByID(self, user_id):
        if not user_id in self.user:
            self.user[user_id] = User(user_id)
        return self.user[user_id]
    
    def getItemByID(self, item_id):
        pass

try:
    CacheData
except NameError:
    CacheData = cacheData()
    
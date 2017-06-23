# -*- coding: utf-8 -*-
from lib.db_con import MySQL

class User:
    def __init__(self, user_id):
        '''最后10次三级目录浏览'''
        self.user_id = user_id
        self.last_ten_cat = []
        self.initCategory()
        
    async def initCategory(self):
        _sql = '''SELECT a.detail, b.thirdcategory_id 
          FROM behavior_browse_item a, item b 
          WHERE a.user_id = %s and a.detail = b.id
          ORDER BY id DESC limit 20;'''
        result = yield MySQL.execute(_sql, (self.user_id, ))
        self.last_ten_cat = result
        return self
            
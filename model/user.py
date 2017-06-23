# -*- coding: utf-8 -*-
from lib.db_con import Execute

class User:
    def __init__(self, user_id):
        '''最后10次三级目录浏览'''
        self.user_id = user_id
        self.last_cat = []
        
    async def initCategory(self, total_amount = None):
        total_amount = 20 if total_amount is None else total_amount
        _sql = '''SELECT b.thirdcategory_id 
          FROM behavior_browse_item a, item b 
          WHERE a.user_id = %s and a.detail = b.id
          ORDER BY a.id DESC LIMIT %s;'''
        result = await Execute(_sql, (self.user_id, total_amount))
        result.reverse()
        self.last_cat = result
        return self
            
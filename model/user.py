# -*- coding: utf-8 -*-
from queue import Queue
from lib.db_con import Execute

class Item(object):
    def __init__(self, init_obj):
        if isinstance(init_obj, dict):
            third = self.__initFromDict(init_obj, 'third')
            brand = self.__initFromDict(init_obj, 'brand')
            series = self.__initFromDict(init_obj, 'series')
        elif isinstance(init_obj, list):
            tp_third, tp_brand, tp_series = init_obj
            third, brand, series = self.__dataClean(tp_third), \
                                   self.__dataClean(tp_brand), \
                                   self.__dataClean(tp_series)
        self.third, self.brand, self.series = third, brand, series
            
    def __dataClean(self, dirty_value):
        dirty_value = str(dirty_value)
        if dirty_value.isdigit():
            return int(dirty_value)
        if dirty_value.upper() in ('NULL', 'NONE'):
            return 0
        return dirty_value
            
    def __initFromDict(self, init_dict, init_key):
        '''对传入的字典可能出现的异常进行统一处理'''
        if init_key is None:
            return
        init_value = init_dict.get(init_key, 0)
        return self.__dataClean(init_value)


class User:
    QUEUE_SIZE = 20
    def __init__(self, user_id):
        '''最后10次三级目录浏览'''
        self.user_id = user_id
        self.last_cat = Queue(self.QUEUE_SIZE)
        
    async def initCategory(self, total_amount = None):
        total_amount = self.QUEUE_SIZE if total_amount is None else total_amount
        _sql = '''SELECT b.thirdcategory_id, b.brand_name, b.series_id
          FROM behavior_browse_item a, item b 
          WHERE a.user_id = %s and a.detail = b.id
          ORDER BY a.id DESC LIMIT %s;'''
        result = await Execute(_sql, (self.user_id, total_amount))
        result.reverse()
        for item_data in result:
            self.last_cat.put(Item(item_data))
        return self
    
    def updateClick(self, item_info):
        self.last_cat.put(Item(item_info))

            
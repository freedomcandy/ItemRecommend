# -*- coding: utf-8 -*-
import pandas
from collections import defaultdict
from lib.db_con import Execute

class Item(object):
    def __init__(self, init_obj):
        if isinstance(init_obj, dict):
            second = self.__initFromDict(init_obj, 'second')
            third = self.__initFromDict(init_obj, 'third')
            brand = self.__initFromDict(init_obj, 'brand')
            series = self.__initFromDict(init_obj, 'series')
        elif isinstance(init_obj, list) or isinstance(init_obj, tuple):
            tp_second, tp_third, tp_brand, tp_series = init_obj
            second, third, brand, series =  \
                self.__dataClean(tp_second),\
                self.__dataClean(tp_third), \
                self.__dataClean(tp_brand), \
                self.__dataClean(tp_series)
        self.second, self.third, self.brand, self.series \
            = second, third, brand, series
            
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
    
    def dump(self):
        return self.__dict__

class User:
    QUEUE_SIZE = 20
    def __init__(self, user_id):
        '''最后10次三级目录浏览'''
        self.user_id = user_id
        self.last_view = []
        
    async def initCategory(self, total_amount = None):
        total_amount = self.QUEUE_SIZE if total_amount is None else total_amount
        _sql = \
        '''SELECT b.subcategory_id, b.thirdcategory_id, b.brand_name, b.series_id
           FROM behavior_browse_item a, item b 
           WHERE a.user_id = %s and a.detail = b.id
           ORDER BY a.id DESC LIMIT %s;'''
        result = await Execute(_sql, (self.user_id, total_amount))
        result.reverse()
        for item_data in result:
            self.last_view.append(Item(item_data))
        return self
    
    def updateClick(self, item_info):
        if len(self.last_view) >= self.QUEUE_SIZE:
            self.last_view.pop(0)
        self.last_view.append(Item(item_info))
        
    def mlThirdCategory(self):
        view_len, pandas_dict = len(self.last_view), defaultdict(list)
        for index, item_obj in enumerate(self.last_view[:10]):
            next_index = index + 1
            if view_len <= next_index:
                break
            pandas_dict['feature'].append(item_obj.third)
            pandas_dict['label'].append(self.last_view[next_index].third)
        return pandas.DataFrame.from_dict(pandas_dict)
    
    async def mlSecondCategory(self):
        item_obj = self.last_view[-1]
        if not item_obj:
            return pandas.DataFrame()
        _sql = '''SELECT thirdcategory_id, brand_name, series_id
                 FROM item
                 WHERE subcategory_id = %s;'''
        result = await Execute(_sql, (item_obj.second, ))
        pandas_dict = defaultdict(list)
        for data_tuple in result:
            for key_name, item_value in zip(['third', 'brand', 'series'], list(data_tuple)):
                pandas_dict[key_name].append(item_value)
        return pandas.DataFrame.from_dict(pandas_dict)
            
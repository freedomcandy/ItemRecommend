# -*- coding: utf-8 -*-
import pandas
from collections import defaultdict
from lib.db_con import Execute

class DataClean(object):
    @staticmethod
    def deaultInt(base_value):
        if not base_value:
            return 0
        str_value = str(base_value)
        if (not str_value.isdigit()) or (str_value.upper() in ('NULL', 'NONE', )):
            return 0
        return int(base_value)
    
    @staticmethod
    def deaultOther(base_value):
        if (not base_value) or (str(base_value).upper() in ('NULL', 'NONE', )):
            return '其他'
        return str(base_value)

class Item(object):
    def __init__(self, init_obj):
        if isinstance(init_obj, dict):
            second = DataClean.deaultInt(init_obj.get('second', None))
            third = DataClean.deaultInt(init_obj.get('third', None))
            brand = DataClean.deaultOther(init_obj.get('brand', None))
            series = DataClean.deaultInt(init_obj.get('series', None))
        elif isinstance(init_obj, list) or isinstance(init_obj, tuple):
            tp_second, tp_third, tp_brand, tp_series = init_obj
            second, third, brand, series =  \
                DataClean.deaultInt(tp_second),\
                DataClean.deaultInt(tp_third), \
                DataClean.deaultOther(tp_brand), \
                DataClean.deaultInt(tp_series)
        self.second, self.third, self.brand, self.series \
            = second, third, brand, series
    
    def dump(self):
        return self.__dict__

class User:
    QUEUE_SIZE = 20
    def __init__(self, user_id):
        '''最后10次三级目录浏览'''
        self.user_id = int(user_id)
        self.last_view = []
        self.init_cat_flag = False
        '''用来记录上一次随机出的数据'''
        self.recommend_his = []
        self.need_refresh = True
        
    async def initCategory(self, total_amount = None):
        if self.init_cat_flag is True:
            return self
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
        self.init_cat_flag = True
        return self
    
    async def updateClick(self, item_info):
        if self.init_cat_flag is True:
            if len(self.last_view) >= self.QUEUE_SIZE:
                self.last_view.pop(0)
            self.last_view.append(Item(item_info))
        else:
            await self.initCategory()
        self.need_refresh = True
        
    def setRecommend(self, recommend_list):
        self.need_refresh = False
        self.recommend_his = recommend_list
        
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
        if not self.last_view:
            return pandas.DataFrame()
        item_obj = self.last_view[-1]
        if not item_obj:
            return pandas.DataFrame()
        _sql = '''SELECT id, thirdcategory_id, brand_name, series_id
                 FROM item
                 WHERE subcategory_id = %s;'''
        result = await Execute(_sql, (item_obj.second, ))
        pandas_dict = defaultdict(list)
        for data_tuple in result:
            for (key_name, Tran_Func), item_value in \
                                        zip([('id', DataClean.deaultInt),
                                             ('third', DataClean.deaultInt), 
                                             ('brand', DataClean.deaultOther), 
                                             ('series', DataClean.deaultInt)], \
                                            list(data_tuple)):
                pandas_dict[key_name].append(Tran_Func(item_value))
        return pandas.DataFrame.from_dict(pandas_dict)
            
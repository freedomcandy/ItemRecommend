# -*- coding: utf-8 -*-
from model.cache import CacheData
from lib.db_con import Execute
from ml.multi_percept import MLP
from random import sample

class conversionTool(object):
    async def converTCtoItem(self, thirdcat):
        _sql = '''SELECT id
                  FROM item
                  WHERE thirdcategory_id = %s;
               '''
        result = await Execute(_sql, (thirdcat, ))
        return [item[0] for item in result]
        
    async def getItemFromThird(self, user_obj):
        user_obj = await user_obj.initCategory()
        df_obj = user_obj.mlThirdCategory()
        if df_obj.empty():
            return []
        third_id = MLP.processMLPClassifier(user_obj.user_id, df_obj)
        item_ref = await self.converTCtoItem(third_id)
        return list(item_ref)
    
    async def getItemFromSecond(self, user_obj):
        user_obj = await user_obj.initCategory()
        second_info = await user_obj.mlSecondCategory()
        if second_info.empty():
            return []
        index_list = MLP.getTargetItemCluster(second_info)
        id_list = second_info.get('id')
        return [int(id_list[index]) for index in index_list]
    
    async def randomGetItems(self, user_id):
        user_obj = CacheData.getUserByID(user_id)
        if user_obj.need_refresh is False:
            return user_obj.recommend_his
        third_result = await self.getItemFromThird(user_obj)
        seconde_result = await self.getItemFromSecond(user_obj)
        finall_set = set(third_result) | set(seconde_result)
        user_obj.setRecommend(sample(list(finall_set), min(len(finall_set), 20)))
        return user_obj.recommend_his
        
try:
    ConTool
except NameError:
    ConTool = conversionTool()
        
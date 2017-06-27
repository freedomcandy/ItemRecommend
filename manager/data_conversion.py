# -*- coding: utf-8 -*-
from lib.db_con import Execute
from model.user import User
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
        
    async def getItemFromThird(self, user_id):
        user_obj = await User(user_id).initCategory()
        df_obj = user_obj.mlThirdCategory()
        third_id = MLP.processMLPClassifier(user_obj.user_id, df_obj)
        item_ref = await self.converTCtoItem(third_id)
        return list(item_ref)
    
    async def getItemFromSecond(self, user_id):
        user_obj = await User(user_id).initCategory()
        second_info = await user_obj.mlSecondCategory()
        index_list = MLP.getTargetItemCluster(second_info)
        id_list = second_info.get('id')
        return [int(id_list[index]) for index in index_list]
    
    async def randomGetItems(self, user_id):
        third_result = await self.getItemFromThird(user_id)
        seconde_result = await self.getItemFromSecond(user_id)
        finall_set = set(third_result) | set(seconde_result)
        return sample(list(finall_set), min(len(finall_set), 20))
        
try:
    ConTool
except NameError:
    ConTool = conversionTool()
        
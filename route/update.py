# -*- coding: utf-8 -*-
import json
import tornado.web
from model.cache import CacheData
from manager.data_conversion import ConTool

class ItemClick(tornado.web.RequestHandler):
    async def post(self):
        user_id = self.get_argument('user_id', 0)
        item_dict = json.loads(self.get_argument('item_dict', '{}'))
        if (user_id == 0) or (not item_dict):
            return self.write(json.dumps({'code': 400}))
        user = CacheData.getUserByID(int(user_id))
        if user is None:
            return self.write(json.dumps({'code': 401}))
        await user.updateClick(item_dict)
        return self.write(json.dumps({'code': 200}))
    
class ItemRecommend(tornado.web.RequestHandler):
    async def get(self):
        user_id = self.get_argument('user_id', 0)
        result = await ConTool.randomGetItems(user_id)
        self.write(json.dumps({'code': 200 ,'items':result}))
    
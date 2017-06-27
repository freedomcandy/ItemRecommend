import json
import tornado.web
from model.cache import CacheData

class ItemClick(tornado.web.RequestHandler):
    async def post(self):
        user_id = self.get_argument('user_id', 0)
        item_dict = json.loads(self.get_argument('item_dict', '{}'))
        if (not user_id) or (not item_dict):
            return self.write(json.dumps({'code': 400}))
        user = CacheData.getUserByID(int(user_id))
        if user is None:
            return self.write(json.dumps({'code': 401}))
        await user.updateClick(item_dict)
        return self.write(json.dumps({'code': 200}))
            
        
        
        
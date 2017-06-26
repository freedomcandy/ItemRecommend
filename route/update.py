import json
import tornado.web
from manager.service import Service

class ItemClick(tornado.web.RequestHandler):
    def post(self):
        user_id = self.get_argument('user_id', 0)
        item_dict = json.loads(self.get_argument('item_dict', '{}'))
        if (not user_id) or (not item_dict):
            return self.write(json.dumps({'code': 400}))
        user = Service.getUser(int(user_id))
        if user is None:
            return self.write(json.dumps({'code': 401}))
        user.updateClick(item_dict)
        return self.write(json.dumps({'code': 200}))
            
        
        
        
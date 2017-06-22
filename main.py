import tornado.ioloop
import tornado.web
import ml.multi_percept as mlp
import json

class ItemRecommendRegressionHandler(tornado.web.RequestHandler):
    def post(self):
        features_data = eval(self.get_argument('tapID', '[]'))
        labels_data = eval(self.get_argument('tapedID', '[]'))
        item_ids = eval(self.get_argument('itemIDs', '[]'))
        #process category predict
        if len(features_data) < 1:# no features  no process
            self.write('No data')
            return
        test_labels = labels_data[len(labels_data) - 1]#get the last one to predict next tap features
        third_category_id = mlp.MultiLayerPerceptron().processMLPClassifier(features_data, labels_data, test_labels)
        obj = {'categoryIds':third_category_id}
        self.write(json.dumps(obj))
        #process itemId clutser
        if len(item_ids) < 1:
            print('1111')
            
#         self.write('Request OK %s' % test_labels)
        

    def get(self):
        self.write('get OK')
    
class ItemRecommendSVCHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('SVC GET OK')
        
    def post(self):
        feature_train = eval( self.get_argument('tapID', '[]' ))
        label_train = int(self.get_argument('tapedID', '[]' ))
        print(feature_train)
        

if __name__ == "__main__":
#     application = tornado.web.Application(autoreload=True)
    application = tornado.web.Application([
        (r'/itemRec', ItemRecommendRegressionHandler)
        ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
#     server = tornado.httpserver.HTTPServer(application)
#     server.listen(8888)
#     instance = tornado.ioloop.IOLoop.instance()
#     tornado.autoreload.start(instance)
#     instance.start()

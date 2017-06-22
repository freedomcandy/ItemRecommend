import tornado.ioloop
import tornado.web
import ml.multi_percept as mlp
import ml.support_vector_classifier as svmc
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
    

#use svm's SVC to predict category_id
class ItemRecommendSVCHandle(tornado.web.RequestHandler):
    def post(self):
        feature_train = eval(self.get_body_argument('tapID', '[]' ))
        label_train = eval(self.get_body_argument('tapedID', '[]' ))
        print(self.get_body_argument('tapID', '[]' ))
        print(self.get_body_argument('tapedID', '[]' ))
        if len(feature_train) < 1:
            self.write('NO TRAINING DATA')
            return
        feature_test = label_train[len(label_train)-1]
        predict_data = svmc.SupportVectorClassifier().processSVMClassifier(feature_train, label_train, feature_test)
        result_data = {'categoryIds':predict_data}
        self.write(json.dump(result_data))

    def get(self):
        self.write('SVC GET OK')

if __name__ == "__main__":
#     application = tornado.web.Application(autoreload=True)

#     application = tornado.web.Application([
#         (r'/itemRec', ItemRecommendRegressionHandler)
    application = tornado.web.Application([
        (r'/itemRec', ItemRecommendHandle),
        (r'/itemRecSVC', ItemRecommendSVCHandle)
        ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
#     server = tornado.httpserver.HTTPServer(application)
#     server.listen(8888)
#     instance = tornado.ioloop.IOLoop.instance()
#     tornado.autoreload.start(instance)
#     instance.start()

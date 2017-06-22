import tornado.ioloop
import tornado.web


class ItemRecommendRegressionHandler(tornado.web.RequestHandler):
    def post(self):
        features_data = self.get_argument('tapID', [])
        labels_data = self.get_argument('tapedID', [])
        item_ids = self.get_argument('itemIDs', [])
        #process category predict
        if len(features_data) < 1:# no features  no process
            self.write('No data')
            return
        test_labels = labels_data[len(labels_data) - 1]
        
        
        #process itemId clutser
        if len(item_ids) < 1:
            print('1111')
            
        self.write('Request OK %s' % test_labels)
        

    def get(self):
        self.write('get OK')
    


if __name__ == "__main__":
#     application = tornado.web.Application(autoreload=True)
    application = tornado.web.Application([
        (r'/', ItemRecommendRegressionHandler)
        ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
#     server = tornado.httpserver.HTTPServer(application)
#     server.listen(8888)
#     instance = tornado.ioloop.IOLoop.instance()
#     tornado.autoreload.start(instance)
#     instance.start()

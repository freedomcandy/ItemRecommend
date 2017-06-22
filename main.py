import tornado.ioloop
import tornado.web
from twisted.web.test.test_tap import application


class ItemRecommendRegressionHandler(tornado.web.RequestHandler):
    def post(self):
        self.write('Request OK')

    def get(self):
        self.write('get OK')
    


if __name__ == "__main__":
#     application = tornado.web.Application(autoreload=True)
    application = tornado.web.Application([
        (r'/',ItemRecommendRegressionHandler)
        ],autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
#     server = tornado.httpserver.HTTPServer(application)
#     server.listen(8888)
#     instance = tornado.ioloop.IOLoop.instance()
#     tornado.autoreload.start(instance)
#     instance.start()
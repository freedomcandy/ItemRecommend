import tornado.ioloop
import tornado.web

if __name__ == "__main__":
    application = tornado.web.Application(autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
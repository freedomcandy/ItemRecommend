import tornado.ioloop
import tornado.web
from route.update import ItemRecommend, ItemClick
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore") 
    application = tornado.web.Application([
        (r'/getRecommend', ItemRecommend),
        (r'/updateClick', ItemClick) 
        ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

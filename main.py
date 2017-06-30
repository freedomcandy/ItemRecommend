import warnings
import tornado.ioloop
import tornado.web
from lib import setting
from route.update import ItemRecommend, ItemClick

if __name__ == "__main__":
    warnings.filterwarnings("ignore") 
    application = tornado.web.Application([
        (r'/getRecommend', ItemRecommend),
        (r'/updateClick', ItemClick) 
        ], autoreload = setting.AUTO_LOAD)
    application.listen(setting.PORT)
    tornado.ioloop.IOLoop.current().start()

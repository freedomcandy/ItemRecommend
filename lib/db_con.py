from setting import sql_conf
from tornado_mysql import pools

pools.DEBUG = True

MySQL = pools.Pool(sql_conf)


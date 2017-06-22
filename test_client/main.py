import urllib
from tornado import httpclient, ioloop

def http_test():
    test_client = httpclient.HTTPClient()
    try:
        response = test_client.fetch('http://172.16.12.50:8888/itemRec',
                                     method = 'POST',
                                     body = urllib.parse.urlencode(\
                                                {'tapID': [1,2,3,4,5],
                                                'tapedID': [2,3,4,5,6]}))
    except Exception as e:
        raise e
    print(response.body)
    
if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(http_test)
        

# -*- coding: utf-8 -*-
from collections import OrderedDict

__all__ = ['LRUCache', ]

class LRUCache(dict):
    '''简单lru队列实现'''
    def __init__(self, size = None):
        self.buff_size = 100 if size is None else size
        self.__cache = OrderedDict()
        
    def __getitem__(self, *args, **kwargs):
        _key = args[0]
        if _key in self.__cache:
            self.__cache[_key] = self.__cache.pop(_key)
        return self.__cache.get(_key, None)
    
    def __setitem__(self, *args, **kwargs):
        _key, _value = args
        if _key in self.__cache:
            self.__cache.pop(_key)
        elif self.buff_size == len(self.__cache):
            self.__cache.popitem(last = False)
        self.__cache[_key] = _value
        
    def __delitem__(self, *args, **kwargs):
        return self.__cache.__delitem__(*args, **kwargs)
        
    def __repr__(self):
        return dict(self.__cache).__repr__()
    
    def items(self):
        return self.__cache.items()
    
    def values(self):
        return self.__cache.values()
    
    def keys(self):
        return self.__cache.keys()
        
if __name__ == '__main__':
    test_cache = LRUCache(3)
    for num in range(5):
        test_cache[num] = num
    print(test_cache)
    

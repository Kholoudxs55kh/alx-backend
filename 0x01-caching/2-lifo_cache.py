#!/usr/bin/env python3
"""
task 2
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    anything
    """
    def __init__(self):
        """
        anything
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        anything
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    last_key, _ = self.cache_data.popitem(True)
                    print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            return

    def get(self, key):
        """
        anything
        """
        return self.cache_data.get(key, None)

# https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheinfo = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cacheinfo:
            self.cacheinfo.move_to_end(key)
            return self.cacheinfo[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheinfo:
            self.cacheinfo[key] = value
            self.cacheinfo.move_to_end(key)
        else:
            if len(self.cacheinfo) == self.capacity:
                self.cacheinfo.popitem(last=False)

        self.cacheinfo[key] = value
        self.cacheinfo.move_to_end(key)
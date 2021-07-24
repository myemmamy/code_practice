# https://leetcode.com/problems/lfu-cache/
#
# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#
# Implement the LFUCache class:
#
# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
#
# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
#
# The functions get and put must each run in O(1) average time complexity.
#
# Example 1:
#
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3

class LFUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.keysfreq = {}

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        if key not in self.keysfreq:
            return -1

        freq = self.keysfreq[key]

        val = self.cache[freq][key]
        if len(self.cache[freq]) == 1:
            del self.cache[freq]
        else:
            del self.cache[freq][key]
        self.keysfreq[key] += 1
        newfreq = self.cache.get(self.keysfreq[key], 0)
        if newfreq == 0:
            self.cache[self.keysfreq[key]] = OrderedDict()
        self.cache[self.keysfreq[key]][key] = val

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        # get key frequence
        freq = self.keysfreq.get(key, 0)

        # hit cache
        if freq != 0:
            if len(self.cache[freq]) == 1:
                del self.cache[freq]
            else:
                del self.cache[freq][key]  # remove from curerrent cache freq list
            freq += 1
            self.keysfreq[key] = freq  # update key freq

        # not hit cache
        else:
            if len(self.keysfreq) == self.capacity:  # cache is full

                # delete one least freq used item
                leastfreq = min(self.cache)

                if len(self.cache[leastfreq]) == 1:  # only one item in the list
                    k, v = self.cache[leastfreq].popitem(last=False)

                    del self.cache[leastfreq]
                    del self.keysfreq[k]

                else:

                    k, v = self.cache[leastfreq].popitem(last=False)
                    del self.keysfreq[k]

            freq = 1
            self.keysfreq[key] = freq  # update key freq

        # new cache list
        freqQ = self.cache.get(freq, 0)  # get new key freq
        if freqQ == 0:
            self.cache[freq] = OrderedDict()
        self.cache[freq][key] = value  # update cache
        # print(self.cache)
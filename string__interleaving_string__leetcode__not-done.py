# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2
# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.
#
# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
############################################################

#part of method 2
def cache(func):
    data={}
    def wrapper(*args):
        if (args) in data:
            return data[(args)]
        else:
            res=func(*args)
            data[(args)] = res
            return res
    return wrapper

class Solution:
    #method 1: use lru_cache directly
    # from functools import lru_cache
    # @lru_cache(None)
    
    #method 2: use decorator
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        return (s1[0] == s3[0] and self.isInterleave(s1[1:],s2,s3[1:])) or (s2[0] == s3[0] and self.isInterleave(s1,s2[1:],s3[1:]))
    

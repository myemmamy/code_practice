# https://leetcode.com/problems/top-k-frequent-words/
# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.

# Try to solve it in O(n log k) time and O(n) extra space.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #nlogk by using heap
        from collections import Counter
        import heapq
        
        cwords = Counter(words)
        res = []
        for x,y in cwords.items():
            heapq.heappush(res,(-y,x))
        #res = [(-y,x) for x,y in cwords.items()] ##not fast as above heappush
        res = heapq.nsmallest(k,res)
        return [y for x,y in res]
            
#        nlogn by using sort
#         d = {}
#         for word in words:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#         wordlist = sorted(d.items(),key=lambda x:(-x[1],x[0]))

#         r = []
#         print(wordlist)
#         for i,(x,y) in enumerate(wordlist):
#             if i < k:
#                 r.append(x)
#             else:
#                 break
#         return r

# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
#
# Example 4:
#
# Input: s = "ac"
# Output: "a"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #odd length palindome and even length palindome checking is different
        #both func return the longest palindome substring length
        def checkOddPalindome(s, i):
            j = 1
            while i - j >= 0 and i + j < len(s):
                if s[i - j] == s[i + j]:
                    j += 1
                else:
                    break
            return (j - 1) * 2 + 1

        def checkEvenPalindome(s, i):
            j = 1
            while i - j >= 0 and i + j + 1 < len(s):
                if s[i - j] == s[i + 1 + j]:
                    j += 1
                else:
                    break
            return (j - 1) * 2 + 2

        pos = 0
        maxlen = 0
        isOdd = True
        for i in range(len(s)):
            oddlen = checkOddPalindome(s, i)
            #check if need to do a even length palindome checking
            if i + 1 < len(s) and s[i] == s[i + 1]:
                evenlen = checkEvenPalindome(s, i)
            else:
                evenlen = 0
            #when find the longer panlindome substring, record it's index
            if oddlen > evenlen and oddlen > maxlen:
                isOdd = True
                pos = i
                maxlen = oddlen
            elif evenlen > oddlen and evenlen > maxlen:
                isOdd = False
                pos = i
                maxlen = evenlen
        # print(pos,maxlen,isOdd)

        return s[pos - maxlen // 2:pos + maxlen // 2 + 1] if isOdd else s[pos + 1 - maxlen // 2:pos + maxlen // 2 + 1]

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
#
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
#
# Note: You are not allowed to use any built-in library method to directly solve this problem.
#
# Example 1:
#
# Input: num = 26
# Output: "1a"
#
#
# Example 2:
#
# Input: num = -1
# Output: "ffffffff"

class Solution:
    import math
    def toHex(self, num: int) -> str:
        if num == 0:  # otherwise get math domain error when run math.log(num,16)
            return '0'
        hexstr = ['a', 'b', 'c', 'd', 'e', 'f']
        nl = []
        if num < 0:
            num = 4294967296 + num

        print(num)
        powern = int(math.log(num, 16))
        while powern >= 0:
            # powern = int(math.log(num,16))
            n = num // int(math.pow(16, powern))
            if n > 9:
                s = hexstr[n - 10]
            else:
                s = str(n)
            nl.append(str(s))
            num -= int(math.pow(16, powern) * n)
            powern -= 1

        return ''.join(nl)



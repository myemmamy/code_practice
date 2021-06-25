# https://www.dailycodingproblem.com/solution/58?token=d115af37b53269d2453f5c0c95464e13445e0020e142285c14b6afbb8c4d4055418bc124
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.

def getItem(arr,val):
    l=len(arr)
    if val == arr[0]:
        return 0
    if val == arr[l-1]:
        return l-1
    pos = l // 2
    if val == arr[pos]:
        return pos
    if arr[pos] < val < arr[-1] or (val < arr[0] and val < arr[pos]):
        return getItem(arr[pos:],val)+pos
    if arr[0] < val < arr[pos] or (val > arr[0] and val > arr[pos]):
        return getItem(arr[:pos],val)

if __name__ == '__main__':
    arr=[13,18,25,30,1,2,8,10]
    print(getItem(arr,2))
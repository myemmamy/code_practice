# https://www.hackerrank.com/challenges/tutorial-intro/problem
#
# In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?
#
# Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.
#
# In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.
#
# Example.
# n=7
# arr = [3,4,7,5,6,2,1]
#
#
#
# Working from left to right, we get the following output:
#
# 3 4 7 5 6 2 1
# 3 4 7 5 6 2 1
# 3 4 5 7 6 2 1
# 3 4 5 6 7 2 1
# 2 3 4 5 6 7 1
# 1 2 3 4 5 6 7

# Sample Input
#
# STDIN           Function
# -----           --------
# 6               n = 6
# 1 4 3 5 6 2     arr = [1, 4, 3, 5, 6, 2]
# Sample Output
#
# 1 4 3 5 6 2
# 1 3 4 5 6 2
# 1 3 4 5 6 2
# 1 3 4 5 6 2
# 1 2 3 4 5 6

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        val = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > val:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = val
                break
            if j == 0:
                arr[0] = val
        line = ' '.join([str(v) for v in arr])
        print(line)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
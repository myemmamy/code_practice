# https://www.hackerrank.com/challenges/quicksort1/problem
# we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:
#
# Step 1: Divide
# Choose some pivot element, p , and partition your unsorted array, arr , into three smaller arrays:  left, right , and equal,
# where each element in left < p , each element in right > p , and each element in equal = p.
#
# Example
# arr =[5,7,4,3,8]
#
# In this challenge, the pivot will always be at arr[0], so the pivot is 5.
#
# arr is divided into left=[4,3] , equal=[5] , and right = [7,8] .
# Putting them all together, you get  [4,3,5,7,8].
# There is a flexible checker that allows the elements of left and right to be in any order. For example, [3,4,5,8,7] is valid as well.

def quickSort(arr):
    # Write your code here
    leftarr=[]
    rightarr=[]
    p=arr[0]
    middlearr=[p]
    for i in range(1,len(arr)):
        if arr[i] < p:
            leftarr.append(arr[i])
        elif arr[i] == p:
            middlearr.append(arr[i])
        else:
            rightarr.append(arr[i])
    result = leftarr+middlearr+rightarr
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

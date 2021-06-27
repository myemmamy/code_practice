# https://www.hackerrank.com/challenges/countingsort3/problem

def getNums(n, arr):
    arr1 = [0] * 15
    for x, y in arr:
        arr1[int(x)] += 1
    print(arr1)

    arr2=[]
    for i in range(len(arr1)):
        if i == 0:
            arr2.append(arr1[i])
        else:
            arr2.append(arr1[i] + arr2[-1])
    print(' '.join([str(v) for v in arr2]))


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(input().strip().split())
    getNums(n, arr)
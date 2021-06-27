https://www.hackerrank.com/challenges/quicksort2/problem


def quicksort(n, arr):
    if n <= 1:
        return arr
    larr = []
    rarr = []
    earr = [arr[0]]
    p = arr[0]
    for i in range(1, n):
        if arr[i] > p:
            rarr.append(arr[i])
        elif arr[i] == p:
            earr.append(arr[i])
        else:
            larr.append(arr[i])
    larr = quicksort(len(larr), larr)
    rarr = quicksort(len(rarr), rarr)
    print(' '.join([str(i) for i in larr + earr + rarr]))
    return larr + earr + rarr


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    quicksort(n, arr)

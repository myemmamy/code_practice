# https://www.hackerrank.com/challenges/quicksort3/problem

#time complexity
# https://www.youtube.com/watch?v=-qOVVRIZzao
# https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/analysis-of-quicksort

# Enter your code here. Read input from STDIN. Print output to STDOUT
def quickSortInplace(arr, start, end):
    if end <= start:
        return
    i = start
    p = arr[end]
    isLarger = False
    for j in range(start, end):
        if arr[j] < p:
            if isLarger:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] >= p:
            isLarger = True
    if isLarger:
        arr[i], arr[end] = arr[end], arr[i]
    # print(arr)

    print(' '.join([str(k) for k in arr]))
    quickSortInplace(arr, start, i - 1)
    quickSortInplace(arr, i + 1, end)
    return arr


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    quickSortInplace(arr, 0, n - 1)





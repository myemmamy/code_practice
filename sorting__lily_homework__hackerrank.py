# https://www.hackerrank.com/challenges/lilys-homework/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def lilysHomework(arr):
    arrD=arr.copy()
    sarr=sorted(arr)
    sarrD=sorted(arr,reverse=True)
    num1,num2 = 0
    for i in range(len(arr)):
        if sarr[i] != arr[i]:
            pos = sarr.index(arr[i])
            arr[i],arr[pos] = arr[pos],arr[i]
            num1 += 1
    for i in range(len(arrD)):
        if sarrD[i] != arrD[i]:
            pos = sarr.index(arrD[i])
            arrD[i],arrD[pos] = arrD[pos],arrD[i]
            num2 += 1
    return min(num1,num2)
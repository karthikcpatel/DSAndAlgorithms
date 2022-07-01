def rotate(arr,n):
    temp = arr[n-1]
    i = n-1
    while(i>0):
        arr[i] = arr[i-1]
        i = i -1
    arr[i] = temp
    print(arr)

arr = [9,8,7,6,4,2,1,3]
n = 8
rotate(arr,n)
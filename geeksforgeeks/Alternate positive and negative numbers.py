#Amazon #Paytm #VMWare #Microsoft #Intuit

def rearrange(arr,n):
    # code here
    negative = []
    positive = []
    for i in range(n):
        if arr[i] < 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    i = 0
    j = 0
    k = 0
    while (i < len(negative) and j < len(positive)):
        if k % 2 == 0:
            arr[k] = positive[j]
            j += 1
            k += 1
        else:
            arr[k] = negative[i]
            k += 1
            i += 1
    if i == len(negative):
        for t in range(k, n):
            arr[t] = positive[j]
            j += 1
    elif j == len(positive):
        for s in range(k, n):
            arr[s] = negative[i]
            i += 1
    print(arr)

arr = [-5, -2, 5]
n = 3
rearrange(arr,n)
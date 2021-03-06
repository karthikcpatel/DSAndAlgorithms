def print_rangoli(n):
    string = "abcdefghijklmnopqrstuvwxyz"
    data = [string[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# URL for reference - https://www.thepoorcoder.com/alphabet-rangoli/
# n = 3
# line 3 can be replaced by for loop using below syntax:
# string = []
# for i in range(n)
#   string.append(i)
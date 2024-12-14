list = ["a", "b", "a", "c", "c", "a", "c", "k", "z"]
result = {}
for i in list:
    if list.count(i) > 1:
        result[i] = list.count(i)
print(result)

list = [10,10,20,30,40,50]
result = {}
for i in list:
    if list.count(i) > 1:
        result[i] = list.count(i)
print(result)


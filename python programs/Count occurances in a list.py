list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
element=2

x=[i for i in list if i==element]

print("The element",element,"occurs",len(x),"times")
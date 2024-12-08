#Sort only first half of the list and append it to second half of the list
list_1 = [30,10,20,80,70,90]
index = 3
first_half = list_1 [:index]
second_half = list_1 [index:]
print('The primary list is: ',list_1)
print("First half of list is ",first_half)
print("Second half of list is ",second_half)
first_half.sort()
print(first_half)
final_list = first_half + second_half

list1 = [10, 43, 0, 27, 98, 0, 75, 0, 59, 191]
print(([x for x in list1 if x]) + [x for x in list1 if not x])

#Get the output in the specific format
string = "Apple~Fruit~100||Cabbage~Vegetable~50||Mango~Fruit~60";
delimiters = ["~", "|"]
for delimiter in delimiters:
    string = " ".join(string.split(delimiter))
result = string.split()
print(result)


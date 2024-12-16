#Sort only first half of the list and append it to second half of the list
# Input list
list_1 = [30, 10, 20, 80, 70, 90]
# Find the midpoint of the list
mid = len(list_1) // 2
# Sort the first half of the list
first_half_sorted = sorted(list_1[:mid])
# Combine the sorted first half with the unchanged second half
result = first_half_sorted + list_1[mid:]
# Output the result
print("Original list:", list_1)
print("List with sorted first half:", result)


# Input list
list1 = [10, 43, 0, 27, 98, 0, 75, 0, 59, 191]
# Separate non-zero and zero elements
non_zero = [num for num in list1 if num != 0]
zero = [num for num in list1 if num == 0]
# Combine non-zero elements followed by zeros
result = non_zero + zero
# Output the result
print("Original list:", list1)
print("List with zeros moved to the end:", result)

#Get the output in the specific format
string = "Apple~Fruit~100||Cabbage~Vegetable~50||Mango~Fruit~60";
delimiters = ["~", "|"]
for delimiter in delimiters:
    string = " ".join(string.split(delimiter))
result = string.split()
print(result)


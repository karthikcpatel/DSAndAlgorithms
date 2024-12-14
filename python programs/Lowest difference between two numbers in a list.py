list = [100,10,20,200,7,50]
list.sort()
least_diff = None
for i in range(len(list)-1):
    diff = abs(list[i] - list[i+1])
    if not least_diff:
        least_diff = diff
    if diff < least_diff:
        least_diff = diff
print(least_diff)

print("********** The below logic also returns the pair **********")

# Input list
list = [100, 10, 20, 200, 7, 50]

# Sort the list
list.sort()

# Initialize variables
least_diff = None
pair = None

# Iterate through the list to find the minimum difference and the corresponding pair
for i in range(len(list) - 1):
    diff = abs(list[i] - list[i + 1])
    if least_diff is None or diff < least_diff:
        least_diff = diff
        pair = (list[i], list[i + 1])  # Store the pair

# Output the results
print(f"Minimum difference: {least_diff}")
print(f"Pair with minimum difference: {pair}")

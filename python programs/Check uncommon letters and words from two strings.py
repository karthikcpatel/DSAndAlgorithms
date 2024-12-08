def UncommonWords(A, B):
    A = A.split()
    B = B.split()
    x = []
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x = list(set(x))
    return x


# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A, B))


print("*************** Second Approach ***************")


list1 = ["Kartik","Chetan","Patel"]
list2 = ["Kartik","Chetankumar","Patel"]

emp_list = []

for i in list1:
    if i not in list2:
        emp_list.append(i)
for i in list2:
    if i not in list1:
        emp_list.append(i)
print(emp_list)
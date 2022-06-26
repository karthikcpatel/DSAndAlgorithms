#Google

# Solution 1:
def areIsomorphic(str1,str2):
    if len(set(zip(str1, str2))) == len(set(str1)) and len(set(zip(str2, str1))) == len(set(str2)):
        print("Solution 1 - Isomorphic")
    else:
        print("Solution 1 - Not isomorphic")

areIsomorphic("aab","xxy")

# Solution 2:
def areIsomorphic(str1,str2):
    dict_str1 = {}
    dict_str2 = {}
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]

    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        print("Solution 2 - Isomorphic")
    else:
        print("Solution 2 - Not isomorphic")

areIsomorphic("aab","xxy")
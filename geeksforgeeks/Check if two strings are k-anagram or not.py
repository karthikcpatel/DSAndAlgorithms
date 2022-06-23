def arekAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    count = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            count += 1
            str2 = str2.replace(str1[i], '', 1)  # for repeating Characters
    if len(str1) - count <= k:
        return True
    return False

# Driver Code
if __name__ == '__main__':
    str1 = "anagram"
    str2 = "grammar"
    k = 2
    if (arekAnagrams(str1, str2, k)):
        print("Yes")
    else:
        print("No")
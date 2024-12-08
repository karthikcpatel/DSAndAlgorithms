# This logic needs to be modified
str1 = "Kartik"
str2 = "Googlek"
set_str1 = set(str1)
set_str2 = set(str2)
common_letters = set_str1 & set_str2
print("The common letters are: ", common_letters)

str1 = "my name is Kartik my"
str2 = "my company is Google"
str1_words = set(str1.split(" "))
print(str1_words)
str2_words = set(str2.split(" "))
print(str2_words)

common_words = (str1_words)&(str2_words)
print("The common words in string are: ",common_words)
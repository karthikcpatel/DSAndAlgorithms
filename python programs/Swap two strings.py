str1 = "Kartik";
str2 = "Patel";
print("Strings before swapping: " +str1+ " " +str2)
str1 = str1 + str2 #KartikPatel
str2 = str1[0: (len(str1) - len(str2))] #11-5=6
print("The value of str2 is: "+str2)
str1 = str1[len(str2):]
print("The value of str1 is: " +str1)
print("Strings after swapping: " +str1+ " " +str2)
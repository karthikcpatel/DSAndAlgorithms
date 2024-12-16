string = "a4b3c2d1"
for i in range(0,len(string)):
    if string[i].isalpha():
        print(string[i]*int(string[i+1]), end = "")

print('\n'"*****************************")

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


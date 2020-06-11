size = int(input("Enter the no of items you want to add in Dictonary: "))
diction = dict()
for i in range(size):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictonary: "))
    diction[key] = value
result = dict()
for key,value in diction.items():
    if value not in result.values():
        result[key] = value
print("Dictonary after removing duplicate values: ", result)

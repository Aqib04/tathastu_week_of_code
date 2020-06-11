size = int(input("Enter the size of tuple: "))
print("Enter the elements in tuple one by one")
arr = []
for i in range(size):
    arr.append(input())
arr = tuple(arr)
element = input("Enter the element whose occurrences you want to know: ")
print("Tuple contains the element", arr.count(element), "times")

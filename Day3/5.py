a= int(input("Enter the no of elements you want to enter in the List 1: "))
list1 = []
for i in range(a):
    list1.append(input())
b= int(input("Enter the no of elements you want to enter in the List 2: "))

list2 = []
for i in range(b):
    list2.append(input())
List3 = list(set(list1).intersection(set(list2)))
print("The intersection of List 1 and List 2 is:", ", ".join(intersectionList))

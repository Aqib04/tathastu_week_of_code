def knapsack(weight, List):
    if weight == 0 or len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0][0] > weight:
            return 0 
        return List[0][1]  
    if List[0][0] > weight:
        return knapsack((weight, List[1:]))
    return max(List[0][1] + knapsack(weight - List[0][0], List[1:]), knapsack(weight, List[1:]))
size =  int(input("Enter the number of items you want to enter: "))
List = []
for i in range(size):
    weight = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    List.append((weight,value))
weight = int(input("Enter the value of weight capacity: "))
print("The maximum value for the given weight " ,weight)
© 2020 GitHub, Inc.

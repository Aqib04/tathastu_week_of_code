def House(List):
    if len(List) == 2:
        return max(List)
    if len(List) == 1:
        return List[0]
    if len(List) == 3:
        return max(List[1], List[0] + House(List[2:]))
    return max(List[1] + House(List[3:]), List[0] + House(List[2:]))
size = int(input("Enter the number of Houses in a line: "))
List = []
for i in range(size):
    List.append(int(input("Enter the value in the House number " + str(i + 1) + ": ")))
print("The maximum stolen value from Houses is", 

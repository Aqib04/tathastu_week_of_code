from itertools import permutations
str=input("Enter any String:-")
pr=permutations(str)
for i in pr:
    print(" ".join(i),end=" ")

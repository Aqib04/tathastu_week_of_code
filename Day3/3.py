s = input('Enter the string:')
f = ''
for i in s:
    if i not in f:
        f += i
print("After remove duplicate",f)

def replace_0_with_5(number):

    return int(str(number).replace('0','5'))

number = int(input("Enter the number you want to check: "))

print("The number after replacing all 0 with 5 will be", replace_0_with_5(number))

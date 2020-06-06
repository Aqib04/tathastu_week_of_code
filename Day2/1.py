n=int(input("Enter The Number \n"))
if n%2==0:
     print("Even")
else:
      print("Odd")
if n>1:
 for i in range(2,n):
  if n%i==0:
  # print(i,"times",num//i,n)
   print("Number is Not Prime",n)
  break
else:
  print("prime number ",n)
  print("prime number ",n)

      
  

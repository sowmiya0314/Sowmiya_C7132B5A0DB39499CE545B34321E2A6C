def factorial(n):
   return 1 if (n==0 or n==1) else n*factorial(n-1)
number=int(input("enter a value"))

print("factorial of",number,"is", factorial(number));
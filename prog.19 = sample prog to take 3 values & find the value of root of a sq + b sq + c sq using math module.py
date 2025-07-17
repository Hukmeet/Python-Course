import math as m
print("This program will help you find the square root of the sum of squares of three numbers.")
A=float(input("Enter the first number:..."))
B=float(input("Enter the second number:..."))
C=float(input("Enter the third number:..."))
a=m.pow(A,2)
b=m.pow(B,2)
c=m.pow(C,2)
sum=a+b+c
root_sum=m.sqrt(sum)
print("Your required output is:",root_sum)

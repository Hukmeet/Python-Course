print("This program will help you verify if\
the given three angles will form a triangle or not.")
a=int(input("Enter the first angle (in degrees) :... "))
b=int(input("Enter the second angle (in degrees) :... "))
c=int(input("Enter the third angle (in degrees) :... "))
sum=a+b+c
if sum ==180:
          print("The angles",a,",",b,"and",c,"will form a triangle.")
else:
          print("The angles",a,",",b,"and",c,"will not form a triangle.")

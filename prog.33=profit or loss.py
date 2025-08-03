print("This program will help you predict if a certain project will g\
o in profit or loss.")
cp=float(input("Enter the Cost Price :... "))
sp=float(input("Enter the Selling Price :... "))
if sp>cp:
          print("Your project will be in a profit of rupees ",(sp-cp),".",sep="")
if cp>sp:
          print("Your project will be in a loss of rupees ",(cp-sp),".",sep="")
if sp==cp:
          print("Your project will neither be in profit nor loss.")

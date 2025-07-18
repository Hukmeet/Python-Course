import math as M
B=float(input("enter the value of base"))
P=float(input("enter the value of perpendicular"))
b=M.pow(B,2)
p=M.pow(P,2)
sum=b+p
root_sum=M.sqrt(sum)
print(int(root_sum))

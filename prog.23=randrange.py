import random as R
import statistics as S
print("Now this program will generate six random integer numbers between 1\
& 50 and find their mean & median")
x1=R.randint(1,50)
print(x1)
x2=R.randint(1,50)
print(x2)
x3=R.randint(1,50)
print(x3)
x4=R.randint(1,50)
print(x4)
x5=R.randint(1,50)
print(x5)
x6=R.randint(1,50)
print(x6)
l=[x1,x2,x3,x4,x5,x6]
mean=S.mean(l)
print("The averqage mean of these values is :",mean)
median=S.median(l)
print("The median of these values is :",median)

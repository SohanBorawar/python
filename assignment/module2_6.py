# A program that swap program between two numbers with temp variable & without temp variable 

print("A program to swap two numbers between each other ")

x = int(input("enter value of X :"))
y = int(input("enter value of Y :"))

temp = x
x=y
y= temp

print("x :",x,"y :",y) 


# without a temp variable 

a = int(input("enter a number a :"))
b = int(input("enter a number b :"))

a,b = b,a

print("a :",a,"b :",b) 


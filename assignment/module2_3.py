# A program to print fibonacci series of given number 

print(">>>>>>>>TO print Fibonacci series of given number ")

n = int(input("Entered number N:"))

a,b=0,1

print(a,end=' ')

while b<n:
    print(b,end=' ')
    a,b=b,a+b

print("print fibonic series by users given input")

n=int(input('enter the number :'))
a,b=0,1

print(a,end='')

while b<n:
    print(b,end='')
    a,b=b,a+b
    print()


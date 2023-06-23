def evenodd(a):
    if a % 2== 0:
        print(a," is even number")
    else:
        print(a," is odd number")

def greater2(a,b):
    if a>b:
        print(a," is greater")
    else:
        print(b," is greater") 

def greater3(a,b,c):
    if a>b:
        if a>c:
            print(a," is greater")
        else:
            print(c," is greater")
    else:
        if b>c:
            print(b," is greater")
        else:
            print(c," is greater")                

def primenumber(n):
    if n % 2 !=0:
        for i in range(1,int(n/2)+1,3):
           if n % i ==0:
               print(n," is prime number")
               break
           else:
                print(n,"is not prime number") 
                break   
    else:
        print(n,"is not prime number")

def fibonaci(n):
    a,b=0,1
    print(a,end="")

    while b<n:
        print(b,end="")
        a,b=b,a+b


#primenumber(43)
#fibonaci(100)
evenodd(3)
greater3(400,77,85)
print("different star patterns")


# print number in 1 to 9
for i in range (1,10):
    print(i)
    print()

# print star series 
for j in range (1,10):
    print(j*"*")

# print mirror star triangle 

for k in range (1,10):
    print(" "*(9-k),k*"*")

# reverse triangle 
for l in range (10,0,-1):
    print(l*"*")    

#full triangle 
for m in range (1,10):
    print(" "*(9-m),m*" *")

# reverse full triangle 
for n in range(9,0,-1):
    print(" "*(9-n),n*" *")

# print number in pattern 
for o in range (1,10):
    for p in range (o):
        print(o,end='')
    print()

# print different number series pattern 

for q in range (1,10):
    for r in range (1,q):
        print(r,end='')
    print()

# print mirror number pattern

for s in range (1,10):
    for t in range (1,10-s):
        print(" ",end='')
    for t in range (1,s):
        print(" ",t,end="")
    print()        
     
l = [1,2,3,1.1,True,False,"Tops"," ",1234,54321]

print(l)
l.append(100)
print(l)
l.append("technology")
print(l)
print(l.count(1.1))
print(l.index(2))


l2 = [101,202,303]
l.insert(4,1)
print(l)

l.pop(6)
print(l)

l.extend(l2)
print(l)

l.reverse()
print(l)

l.append(1000)
print(l)

print(l.count(101))
print(l.index(3))
l.insert(4,5000)
print(l)
l.pop(5)

l.reverse()
print(l)
print(l)

print(len(l))
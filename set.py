# set
x=set()
print(type(x))

# add element in a set
x.add(30)
print(x)


x={10,20,30,40,10}
print(x)

# set-->list
xl=list(x)
print(xl[0])

xl[2]=90
print(xl)

# list-->set
x=set(xl)
print(x,type(x))

# different opration on set
A={1,2,3}
B={3,4,1}
print(A.union(B))
print(A|B)

print(A.intersection(B))
print(A&B)

print(A.difference(B))
print(A-B)


print(A.symmetric_difference (B))
print(A^B)

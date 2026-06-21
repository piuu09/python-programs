x=frozenset()
print(x,type(x))

x=frozenset([10,20,30])
print(x,type(x))


for i in x:
    print(i)
print(20 in x)    

x=frozenset((910,20,30))
print(x,type(x))

x=frozenset("hello")
print(x,type(x))
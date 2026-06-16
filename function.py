# without return type
# function without argument without return type
def greet():
    print("hello")

greet()
#----------------------------------------------------------

# function with argument without return type
def cube(num):
    print(num**3)

num=int(input("enter a number:"))
cube(num)   

#----------------------------------------------------------
# with return type
# function without argument with return type
def getNo():
    return 10

# 1 way
op=getNo()
print(op)

# 2 way
print(getNo())

#------------------------------------------------------------
# function with argument with return type
def add(a,b):
    return a+b

print(add(10,20))
print(add(10.2,12.3))


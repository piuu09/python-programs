class demo:
    c_name="xyz"


    def __init__(self):
        print("default constructor called")


# 1 way:-
# classname.varname
print(demo.c_name)  

# 2 way:-
# objectrefvar.varname
obj=demo()
print(obj.c_name)

#------------------------------------------------------
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1=student("ram",90)
print(s1.name) 
print(s1.age)

s2=student("sita",20)
print(s2.name) 
print(s2.age)

     
# ZeroDivison Erroe

print("start")
try:
    print(10/0)
except ZeroDivisionError as e :
    print(e)
print("end")

#--------------------------------------------------------
# ValueError
 
try:
    ip=int(input("enter a number :" ))
    print(ip)
except ValueError as e:
    print(e)  

#-----------------------------------------------------
# IndexError
try:
    x=[10,20,30]
    print(x[7])  
except IndexError as e:
    print(e) 

#------------------------------------------------------------
# multiple except
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)        

#---------------------------------------------------------
try:
    a={"name":"ram"}
    print(a["name"])
    print(a["age"])
except Exception as e:
    print("key not present")
else:
    print("end")
finally:
        print("-----------------------")

#-------------------------------------------------------------------------


try:
    a=int(input(" enter first number:"))
    b=int(input(" enter second number:"))
    def add(a,b):
        return a+b
    print(add(a,b))
except ValueError :  
    print("entre only number")

finally :
    print("-----")




x={}
print(x,type(x))

# add item
x["name"]="ram"
print(x)

# print particular value
print(x["name"])

# update
x["name"]="sita"
print(x)
print(x["name"])

# read data
x[101]="stud data"
print(x)

#delete
del x[101]
print(x)

# pop
print(x.pop("name"))

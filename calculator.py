print(" calculator\n1.add \n2.sub\n3.mul\n4.div\n6.exit\n")
choice=int(input(" enter your choice:"))
num1=int(input(" enter first number:"))
num2=int(input(" enter second number:"))
match choice:
    case 1:
        print(f" add{num1} and {num2} is {num1+num2}")
    case 2:
        print(" sub:",num1-num2)
    case 3:
        print(" mul:",num1*num2)
    case 4:
        print(" div:",num1/num2)

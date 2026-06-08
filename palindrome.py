num=int(input(" enter a number:"))
rev=0
rem=0
num1=num
while num1>0:
    rem=num1%10
    rev=rem+(rev*10)
    num1=num1//10
if num==rev:
    print("palindrome ")
else:
    print(" it is not a palindrome")

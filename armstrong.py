num=int(input("enter any number:"))
sum=0
temp=num
count=0
while temp>0:
    count+=1
    temp=temp//10
temp=num
while(temp>0):
    rem=temp%10
    sum=sum+rem**count
    temp=temp//10
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")

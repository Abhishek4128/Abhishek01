num=int(input("enter a number:"))
sum=0
temp=num
digits=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+digit**digits
    temp=temp//10
if num==sum:
    print(num,"is amstrong number")
else:
    print(num,"not amstrong number")
n=int(input("enter the number:"))
r=n**0.5
count=0
if(n==1):
    print("not a prime number")
elif(n==2):
    print("prime number")
for i in range(2,int(n+1)):
    if(n%i==0):
        count+=1
        break
if(count==0):
    print("prime")
else:
    print("not prime")
    
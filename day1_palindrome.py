num=int(input("enter any number:"))
rem=0
res=0
temp=num
while(num>0):
    rem=num%10
    res=(res*10)+rem
    num=num//10     
if res==temp:
    print("palindrome")
else:
    print("not plaindrome")
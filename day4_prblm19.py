'''mr.x trying to create for his instagram account this are the requried condition for creating a new password
1.min len is 8 max len is 15
2.only @,/ are allowed in a password
3.no spaces are allowed
4.only alpha numeric are allowed, your suppose to print weak if len exact 8,medium len is b/w 8-12,strong len is b/w 12-15 '''

s=input()
n=len(s)
count=0
str="@/"
for i in s:
    if(i==str[0] or i==str[1] or i!=' '):
        count+=1
        break
if(count==0):
    print("please follow the conditions") 
elif(n<8):
    print("please follow the conditions")
elif(n==8):
    print("password is weak")
elif(n>8 and n<12):
    print("password is moderate")
elif(n>=12 and n<15):
    print("password is strong")
else:
    print("very strong")
    



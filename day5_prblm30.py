#print the numeric values in the string and add them 
s="hello1234"
c="1234567"
sum=0
for i in s:
    if(i in c):
        sum+=int(i)
print(sum)

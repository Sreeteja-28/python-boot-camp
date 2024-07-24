
'''****** find the reverse number'''
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
    #convert the number str to int
ans=int(rev)    
print(ans)
print(type(ans))



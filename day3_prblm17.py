'''find the sum even  of in a given number'''
n=int(input())
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum+=r
    n=n//10
print(sum)    
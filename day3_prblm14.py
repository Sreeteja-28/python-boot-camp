'''find the missing number in array'''
arr=list(map(int,input().split(" ")))
k=sum(arr)
print("sum of the list",k)
sum=0
n=int(input())
for i in range(1,n+1):
    sum+=i
print(f"sum of first{n} natural numbers",sum)
print(f"missing nmber",sum-k)

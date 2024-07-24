'''n=int(input())
sum=n*(n+1)//2
print(sum)'''

my_list=list(map(int,input().split()))
sum=0
for i in my_list:
    sum+=1
print(f"sum of all elements in list is {sum}")
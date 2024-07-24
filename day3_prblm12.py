'''find the min element in a given list'''
l=list(map(int,input().split(" ")))
min=l[0]
for i in range(len(l)):
    if(min>l[i]):
        min=l[i]
print(min)
        
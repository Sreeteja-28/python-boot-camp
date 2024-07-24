'''find the duplicate in an array sample input:8 7 7 8 5 4 4 8 9'''
my_list=list(map(int,input().split(" ")))
new=[]
for i in my_list:
    if(i not in new):
        new.append(i)
print(*new)

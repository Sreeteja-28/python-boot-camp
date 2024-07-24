#given any space seperate  integer list find the avg of element  present in the given index
'''my_list=list(map(int,input().split(" ")))
sum=0
n=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
        sum+=my_list[i]
    avg=sum/n
print(avg)'''

my_list=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(len(my_list)):
    if(i%2==0):
        sum+=my_list[i]
        count+=1
print(sum/count)

    
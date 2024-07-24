#7.1 your given with a , seperated natural numbers 1to10 print only even number
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
    count+=1
print(count)
    #print(my_list[i])   
    
#7.2 how many even number are there in above question
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
    count+=1
print(count)

#7.3 given with a space sep integer list find no.of even elements and no.of odd elements in a given list 
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(odd)
print(even)



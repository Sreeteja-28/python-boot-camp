'''find the of element that is present in k+n index
sample i/p k=3 k is given by user 3 6 8 4 61 2 and n=2   o/p is 2
sample2 k=3 ,n=4 elements - 80 70 54 36 72  o/p=error'''

my_list=list(map(int,input().split(" ")))
n=int(input())
k=int(input())
l=len(my_list)
if(l<k+n):
    print("error")
else:
    for i in range(0,l): 
        if(i==k+n):
            print(my_list[i])

'''for i in range(0,l):
       print(my_list[k+n],end=" ") 
        break'''




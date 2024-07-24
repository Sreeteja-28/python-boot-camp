'''peak element'''
n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)-1):
   if(n[i-1]<n[i] and n[i]>n[i+1]):
      count=i
     #print(n[i],end=" ")
if(n[-1]>n[-2] and n[-1]>count): #peak element in last
   count=len(n)-1
print(n[count])        
      
      
      
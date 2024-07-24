#sort elements and 1sthalf in ascending order and 2nd half in desending order

arr=list(map(int,input().split(" ")))
n=len(arr)
print(n)
arr.sort()
print(arr)
n1=n//2
for i in arr[0:n1]:
    print(i,end=" ")
for i in arr[n-1:-n1]:
    print(i,end=" ") 
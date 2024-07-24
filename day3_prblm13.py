'''replace elements in a array with avg of max and min element
sample input : 13 2 67 20 68 output:35 35 35 35 35'''

arr=list(map(int,input().split(" ")))
avg=0
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if(min>arr[i]):
        min=arr[i]

    if(max<arr[i]):
        max=arr[i]
avg=(min+max)//2
for i in range(len(arr)):
    arr[i]=avg
print(arr)




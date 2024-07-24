'''n=int(input())
for i in range(n):
    for j in range(n):
        if(i>j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()'''

'''n=int(input())
for i in range(n):
    for j in range(n):
        if(i<j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()'''


n=[1,2,3,4,5]
for i in n:
    for j in range(1,i+1):
            print(j,end=" ")
    print()
'''print all the prime numbers in given range'''

a=int(input("enter the number:"))
b=int(input("enter the number:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

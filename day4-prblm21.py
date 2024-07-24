'''#gcd of numbers:
#euclidean algorithm:
a=int(input("enter 1st number: "))
b=int(input("enter 2st number: "))
while b!=0:
    a,b=b,a%b
print("gcd of 2 number is:",a)   '''

#LCM of numbers:
a=int(input("enter 1st number: "))
b=int(input("enter 2st number: "))
c,d=a,b
while b!=0:
    a,b=b,a%b
print((c*d)//a)



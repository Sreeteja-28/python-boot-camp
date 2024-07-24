#ascii values starts with 0-122a-z 122-127bracke
print(ord('Y'))
#syntax to know the ascii value
print(ord('s'))
print(ord('0'))
print(ord('<'))
print(chr(122))

#check how many vowels are there in a string
check=['a','e','i','o','u']
count=0
n="hello wOrld"
n=n.lower()
for i in n:
    if(i in check):
        count+=1
print(count)

#ascii value between range
for i in range(32,128):
    print(chr(i),end=" ")



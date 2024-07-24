#write a code to print all the capital letters in a given string
#remove all the brackets from the given algebraic expressions
inp=input()
for i in inp:
    if (ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print()
#converting the interger into ascii
s="hello-----wor--ld"
new=" "
count=0
for i in s:
    if(i=="-"):
         count+=1
    else:
        new+=i
print("-"*count+new,end="")
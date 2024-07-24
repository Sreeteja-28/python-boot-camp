#print all the vowels followed by consonent
s="sreeteja"
con="bcdfghjklmnpqrstvwxyz"
c=""
n=s.lower()
v="aeiou"
for i in s:
    if(i in v):
        c+=i
for i in n:
    if(i in con):
        c+=i
print(c)

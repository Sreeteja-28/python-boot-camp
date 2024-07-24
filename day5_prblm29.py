#check how many consonents in a string
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
input=i.lower()
for i in input:
    if(i in consonent):
        count+=1
print(count)
apples=int(input("no of apples: "))
bananas=int(input("no of bananas: "))
oranges=int(input("no of oranges: "))
ca=int(15)
cb=int(4)
co=int(5)
given=int(input("given money"))
ta=apples*ca
tb=bananas*cb*12
to=oranges*co
sum=ta+tb+to
print(given-sum)
if(sum<=given):
    print("not cheated")
else:
    print("cheated")
age=int(input("enter age of the person: "))
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("four wheeler")
elif(age>45):
    print("all")
else:
    print("cannot drive")
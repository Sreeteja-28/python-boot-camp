#mr z is selected for olympics he is participating in swimming competition only one winner is selected among all the participants and mr x and mr y are friends of z
#mr x is participating in badminton mr y is participating in table tennis according to the selection commitee the requirement for badminton players are
#height 140 cm weight factors of 2 body fat is less than 12% for badminton 
#according to the selection commitee requirements for table tennis are height minimum 118 to 148cm weight no of medals won by mr z body fat 14%
#according to the previous history z participated in 14 games out of which he is having success rate of 65%
#write a program to check whether mr x ,y,z travel in a same plane or not
bh=int(input("height of X"))
bw=int(input("weight of X"))
th=int(input("height of Y"))
tw=int(input("weight of Y"))
fact7=(50*14)/100
if(bh==140 and bw%2==0):
    print("Mr,X is selected")
elif(th<140 and th>118 and tw%fact7==0):
    print("Mr.y is selected ")
else:
    print("Mr.Z is selected")
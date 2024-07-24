#leap year
for i in range(2000,2025):
    if(i%400==0 or i%4==0 and i%100!=0):
     print("leap year",i)
    else:
       print("not leap year",i)



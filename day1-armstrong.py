arm=int(input())
sum=0
copy_arm=arm
no_of_digits=len(str(arm))
while(arm>0):
    digit1=arm%10
    sum+=digit1**no_of_digits
    arm=arm//10
    if sum==copy_arm:
      print(copy_arm ,"is a armstrong")
else: 
  print(copy_arm ,"is a not  armstrong")
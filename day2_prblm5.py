my_list=list(map(int,input().split(",")))
print("choice 1 for append\n choice 2 for pop\n choice 3 for sort\n choice  4 for length\n")
choice=int(input())
if(choice==1):
    my_list.append(6)
    print(*my_list)
elif(choice==2):
    my_list.pop(3)
    print(*my_list)
elif(choice==3):
    my_list.sort()
    print(*my_list)
else:
    print(len(my_list))

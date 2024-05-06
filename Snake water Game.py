import random

def check(comp,user):
    if(comp==user):
        return 0
    elif(comp==0 and user==1):
        return -1
    elif(comp==1 and user==2):
        return -1
    elif(comp==2 and user==1):
        return -1
    
    return 1
print("Lets Play a Snake Game With Computer. ")
comp=random.randint(0,2)
print("Please Select any one these. ")
user=int(input(" 0 for Snake , 1 for Water , 2 for Gun \n"))

score=check(comp,user)

print("You : ",user)
print("Computer : ",comp)


if(score==0):
    print("Its Draw")
elif(score==1):
    print("You Won")
if(score==-1):
    print("You Lose")
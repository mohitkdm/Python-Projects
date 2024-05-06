n=int(input("Enter Your Ist Number : "))
m=int(input("Enter Your Ist Number : "))

user=input("Choose Your operation Add for + , Subs for - , Multi for * , divide for / \n")

print("select user operation is ",user)
if(user=="+"):
    print("The Additiom of",n," And ",m," is: ",n+m)
if(user=="-"):
    print("The Substraction of",n," From ",m," is : ",n-m)
if(user=="*"):
    print("The Multiplication of",n," Or ",m," is : ",n*m)
if(user=="/"):
    print("The Division of",n," By ",m," is : ",n/m)

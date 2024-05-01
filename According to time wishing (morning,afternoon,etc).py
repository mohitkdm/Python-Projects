import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
t=int(time.strftime('%H'))
if(t>0 and t<12):
    print("Good Morning Sir")
elif(t>12 and t<16):
    print("Good Afternoon Sir")
elif(t>16 and t<19):
    print("Good Evening Sir")
elif(t>19 and t<24):
    print("Good Night Sir")
else:
    ("Bye Bye")
print("Have A Nice Day... (.^.)")
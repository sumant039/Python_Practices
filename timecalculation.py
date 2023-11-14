import time
current_time= int(input("Enter your time:- "))
# current_time = time.strftime('%H:%M:%S')
if (current_time < 12):
    print("good Morning",)
elif(current_time < 15):
    print("good Afternoon")
elif(current_time < 21):
    print("good Evening")
elif(current_time <= 24):
    print("good Night")
else:
    print("invlaid number")


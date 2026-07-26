"""Program to Wish the User Good Morning/Good Afternoon/
                        Good Evening/Good Night based on time: """
import time
exacttime=time.strftime('%H:%M:%S')
print(exacttime)
hours=int(time.strftime('%H'))
if(hours>=00 and hours<=11):
    print("Good Morning!!!")
elif(hours>=12 and hours<=17):
     print("Good Afternoon!!!")
elif(hours>=18 and hours<=20):
     print("Good Evening!!!")
else:
     print("Good Night!!!")
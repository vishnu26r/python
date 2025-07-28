import time

my_time = int(input("enter time in seconds: "))


for i in range(0,my_time):
    print(i)
    time.sleep(1)
print("Time's up! buddy")


for i in range(my_time,0,-1):
    print(i)
    time.sleep(1)
print("Time's up guys!!!")




import threading
import time

def walk_dog(name):
    time.sleep(8)
    print(f"You finish walking {name}")

def take_out_trash():
    time.sleep(2)
    print("You are take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# it will run the based function which calls 1st 
#walk_dog()
#take_out_trash()
#get_mail()


#it will run based on threading
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")
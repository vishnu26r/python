#email = "vishnu26.r@gmail.com"

email = input("enter an email:  ")
if "@" in email and ".com" in email:
    print("Valid email")
else:
    print("Not valid ")
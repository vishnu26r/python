#Membership operator  = used to test whether value or variable is found or not in a sequence 
#                     1) in
#                     2) not in 


word ="APPLE"

letter = input("Guess a letter: ").upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} not found")
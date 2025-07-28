import random


#numbers
num = random.randint(1,6)
print(num)
print()

#game
options = ("Rock", "Paper", "Scissors")

choice = random.choice(options)
print(choice)

#cards

cards = ["2","3","4","5","6","7","8","9","10","J","A","Q","A"]
random.shuffle(cards)
print(cards)

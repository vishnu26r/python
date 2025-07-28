menu = { "pizza" : 200.00 , 
        "lemonade" : 100.12 ,
        "hot choclate" : 89.23,
        "briyani" : 100.134,
        "tea" : 10.112   }

cart =[]
total =0
print("----------------MENU-------------")
for key, value in menu.items():
    print(F"{key:15} : ${value:.2f}")
print("---------------------------------")

while True:
    food = input("Select an item ( q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------------YOUR ORDER----------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is {total:.2f} ")
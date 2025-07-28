capitals = { "USA" : "washington D.C" , "India" : "New Delhi", "China" : "Beijing" , "Russia" : "Moscow" }


for i in capitals:
    print(capitals.get(i))

print()
n = input()

#get()

if capitals.get(n):
    print("capital exists")
    print(capitals.get(n))
else:
    print("capital doesn't exists")


print()


#update()
capitals.update({"Germany" : "Berlin"})
capitals.update({"India" : "Tamil Nadu"})
print(capitals)

print()  


#pop()
capitals.pop("China")
print(capitals)

print()
capitals.popitem()
print(capitals)

print()

#key
for key in capitals.keys():
    print(key)

print()

#values()

values = capitals.values()

for value in values:
    print(value)

print()

#items()

items = capitals.items()
print(items)

for key,value in capitals.items():
    print(f" {key} : {value}")
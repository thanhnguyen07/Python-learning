# For
myList = [1 , 2 , 3 , 4]
for item in myList: # for(auto item : myList)
    print(item)

animalLookup = {
    'a' : ['aadvark' , 'antelope'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog'],
}

for letter , animals in animalLookup.items():
    pass
    
# Continue
for letter , animals in animalLookup.items():
    if len(animals) > 1:
        continue
    else:
        print(f"Only one animal: {animals}")
        
# Break
for letter , animals in animalLookup.items():
    if len(animals) > 1:
        print(f"There are {len(animals)} animal: {animals}")
        break
    print(f"Only one animal: {animals}")

# For , else
for number in range (2 , 100):
    for factor in range(2 , int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f"{number} is prime")

for number in range(2 , 100):
    found_factors = False
    for factor in range(2 , int(number**0.5) + 1):
        if number % factor == 0:
            found_factors = True
            break
    if not found_factors:
        print(f"{number} is prime")
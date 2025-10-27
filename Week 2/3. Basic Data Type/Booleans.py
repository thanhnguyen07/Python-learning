# Booleans
# Casting booleans
print(bool(1)) # -> True
print(bool(0)) # -> False
print(bool(-1)) # -> True
print(bool(1j)) # -> True
print(bool(0.0)) # -> False
print(bool(0j)) # -> False
print(bool('True')) # -> True
print(bool('False')) # -> True
print(bool('')) # -> False do nó là empty string
print(bool([])) # -> False do nó là empty list
print(bool({})) # -> False do nó là empty disctionary
print(bool(None)) # -> False 

myList = [1 , 2]
if bool(myList):
    print("My List has some value!")

a = 5
b = 5
if bool(a - b): 
    print("a and b are not equal")
else:
    print("a and b are equal")

weatherIsNice = False
haveUmbrella = True

# Ví dụ của cô giáo
if not weatherIsNice or haveUmbrella:
    print("Stay inside!")
else: 
    print("Go for a walk!")

# Ví dụ của mình
if weatherIsNice:
    print("We can go for a walk")
else:
    if haveUmbrella:
        print("We can go for a walk but it is a bit uncomfortable")
    else:
        print("Nah we can't go for a walk tho")
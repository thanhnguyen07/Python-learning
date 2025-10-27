# Class Inheritance
class Dog:
    _legs = 4
    def __init__(self , name):
        self.name = name
    
    def speak(self):
        print(self.name + " says: Bark!")
        
    def getLegs(self):
        return self._legs

class Chihuahua(Dog):
    def speak(self):
        print(f"{self.name} says: Yap yap yap!")
        
    def wagTail(self):
        print("Vigorous wagging!")
    
dog = Chihuahua("Roxy")
print(dog.speak())
print(dog.wagTail())

myDog = Dog("Rover")
print(myDog.speak())

# Extending built-in classes
myList = list()

class UniqueList(list):
    def __init__(self):
        self.someProperty = "Unique Lists!"
    
    def append(self , item):
        if item in self:
            return
        super().append(item)
        
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)
# Print "Hello World" to the terminal
print('Hello World!')




#02_01 Basic Data Types
# Integer 
x = 5
print(x)

# Float
y = 1.5
print(y)

# String
name = "Ryan"
print(name)
ch1 = "Thanh"
ch2 = " "
ch3 = "Nguyen"
print(ch1 + ch2 + ch3)

# Check the variable 
xau = type(name)
int = type(x)
float = type(y)
print(xau)
print(int)
print(float)

# -> Chỉ sử dụng các phép toán với các dữ liệu có kiểu giống nhau

#Booleans
a = 2
b = 2
c = 3
print(a == b) # -> True vì a = b (2 = 2)
print(a == c) # -> False vì a != c (2 != 3)




#02_02 Data Structure
# List (Mảng)
# Integer List
my_list = [1 , 2 , 3 , 4]
print(my_list)

# String List
my_list = ['list' , 'of' , 'string']
print(my_list)

# Lists of lists
my_list = [[1 , 2 , 3] , [False , True] , [1.23 , 9.52 , 4.21]]
print(my_list)

# Mixed List
my_list = [1 , 'list' , True , []]
print(my_list)

# Sets
my_set = {1 , 2 , 3 , 4}
print(my_set)

# Len function
print(len(my_set))
my_set = {1 , 1 , 2 , 2}
print(len(my_set)) # -> Set -> đếm số lượng số liệu khác nhau 
print(my_set)

# Tuples: Giống với list, nhưng không thể append thêm phần tử
my_tuple = {1 , 2 , 3}
print(len(my_tuple))
# my_tuple.append(4)
# print(my_tuple) -> Thay phần tử 3 thành phần tử 4 ở phía cuối
# Thông thường khi mình thêm một phần tử khác vào list, máy tính liền biết và mở rộng thêm ô
# nhớ để lưu thêm một phần tử, với tuple khi máy tính đọc thì nó chỉ cần lưu giá trị vào bộ
# nhớ với kích thước cố định

# Compare Sets, Lists, Tuples
print([1 , 2] == [1 , 2]) # -> True 
print([1 , 2] == [2 , 1]) # -> False vì sai thứ tự trong list
print({1 , 2} == {2 , 1}) # -> True vì set không xét thứ tự

# Dictionaries
my_dictionary = {
    'apple' : 'A red fruit',
    'bear' : 'A scary animal'
}

print(my_dictionary['apple'])

my_dictionary = {
    'apple' : 'A red fruit',
    'bear' : 'A scary animal',
    'apple' : 'Sometimes it has green color'
}

print(my_dictionary['apple'])
# -> Cả Set và Dictionaries đều không có thứ tự




#02_03 Operator
#Plus Operator
print(1 + 1)

#Multiple Operator
print(5 * 5)

#Exponent Operator
print(5 ** 2)

#Division Operator
print(20 / 5)

#Modulus Operator
print(20 % 7)

#String plus Operator
print("level" + "123")

#String multiplication Operator
print("- string 1 -" * 4)

#Comparison Operator
print(True == True)
print(4 < 5)
print(5 <= 5)
print(5 > 2)

#Logical Operator
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
print(not False)

#Membership Operator
print(1 in [1 , 2 , 3 , 4 , 5])
print(10 in [1 , 2 , 3 , 4 , 5])
print(10 not in [1 , 2 , 3 , 4 , 5])

print("cat" in "my pet cat")




#02_04 Control Flow
#If/Else Statement
a = True
b = True
c = True
if a:
    print("It is true")
    print("Also print this")
    if b:
        print("Both are true")
        if c:
            print("All three are true")
else:
    print("It is False")
print("Always print this")

#For loops
a = [1 , 2 , 3 , 4 , 5]
for item in a:
    print(item)

#While loops
a = 0
while a < 5:
    print(a)
    a = a + 1




#02_05 Functions
def multiplyByThree(val):
    return 3 * val
print(multiplyByThree(4))

def multiply(val1 , val2):
    return val1 * val2
print(multiply(3 , 4))

a = [1 , 2 , 3]
def appendFour(myList):
    myList.append(4)
appendFour(a)
print(a)




#02_06 Classes -> Giống Struct
class Dog:
    def __init__(self , name): #Initialization function
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name +  " says: " + "Bark!")
my_dog = Dog("Rover")
another_dog = Dog("Fluffy")

print(my_dog.speak())
print(another_dog.speak())
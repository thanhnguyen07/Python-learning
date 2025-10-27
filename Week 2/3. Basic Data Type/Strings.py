# Slicing 
name = "My Name is Ryan Mitchell"
# In ra phần tử đầu tiên của String
print(name[0])
# In ra phần tử thứ hai của String
print(name[1])
# In ra trong đoạn ký tự từ 0 -> 7
print(name[0 : 7]) 
# hoặc có thể viết
print(name[:7])
# Viết dấu 2 chấm ở phía trước để in các ký tự ở phía sau
print(name[11:])

myList = [1 , 2 , 3 , 4 , 5]
print(myList[2 : 4])

# List và String có nhiều điểm tương đồng 
print(len(name))
print(len(myList))

# Formatting 
print("My number is: " + str(5))
# In ra string đầu và cộng thêm số 5 đã được ép kiểu từ int -> char

# Dùng thư viện math    
import math
print("Pi is: " + str(round(math.pi , 2)))

# Multi-line Strings
myString = '''
Here is a long block of text
I can add newlines:
The text doesn't stop until it sees \'\'\'
'''
print(myString)

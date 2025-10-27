# Sets
mySet = {'a' , 'b' , 'c'}
print(mySet)
mySet = set(list(mySet))
print(mySet)
# Sets loại bỏ phần tử trùng 
myList = ['a' , 'b' , 'b' , 'c' , 'c' , 'c']
myList = list(set(myList))
print(myList)
# Lệnh add dùng để thêm phần tử
mySet.add('d')
print(mySet)
# Lệnh discard để loại bỏ phần tử 
mySet.discard('d')
print(mySet)
# Kiểm tra phần tử trong set
print('a' in mySet)
# Lệnh len để chỉ ra độ dài
print(len(mySet))

while len(mySet):
    print(mySet.pop())

# Tuples
# Cho phép các phần tử sắp xếp có thứ tự nhưng không thể chỉnh sửa được tuple
myTuple = ('a' , 'b' , 'c')
print(myTuple[0])
# Nó tiện hơn List, nó không quan tâm đến sự thay đổi trong mảng, và lưu trữ trong bộ nhớ

def returnMultipleValue():
    return 1 , 2 , 3

print(type(returnMultipleValue()))
a , b , c = returnMultipleValue()
print(a)
print(b)
print(c)
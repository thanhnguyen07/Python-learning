#Lists
myList = [1 , 2 , 3 , 4 , 5]
# In ra tất cả phần tử sau phần tử thứ 3
print(myList[3:])
# In phần tử trong đoạn từ 0 -> 6 với bước nhẩy 3 phẩn tử
print(myList[0 : 6 : 3])
# hoặc có thể viết
print(myList[::3])

for i in range(100):
    print(i)
# In ra nhiều line và dài -> sử dụng step sẽ nhanh hơn
myList = list(range(100))
print(myList[::2])

# Modifying Lists
myList = [1 , 2 , 3 , 4]
# Lệnh append dùng để thêm phần tử vào cuối list
myList.append(5)
print(myList)
# Lệnh insert dùng để thêm phần tử vào vị trí cụ thể
myList.insert(3 , "a new value")
print(myList) # -> Thêm xâu vào vị trí thứ 3
# Lệnh delete dùng để xóa phần tử cụ thể
myList.remove("a new value")
print(myList)
# Lưu ý nếu xóa một phần tử mà ko có trong List -> Xảy ra lỗi
# Lệnh pop dùng để xóa phần tử ở cuối Lists
myList.pop()
print(myList)

while len(myList):
    print(myList.pop())

print(myList) # -> Mảng này trống

a = [1 , 2 , 3 , 4 , 5]
b = a
a.append(6)
print(b)


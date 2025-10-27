print(20 / 4)
print(4 + 4.0) # -> Đáp án 8.0 do python ưu tiên type float
print(4 * 4.0) 
print(4 ** 4.0)

# Để convert về int thì
print(int(4 ** 4.0))
print(int(8.9))
print(int(8.999999999999999999))
# -> Quy trình casting -> giống ép kiểu trong C++

# Làm tròn số thì dùng hàm round()
print(round(14 / 3)) # -> Đáp án là 5 do nó được làm tròn
print(round(14 / 3 , 2)) # -> Làm trọn 2 chữ số 
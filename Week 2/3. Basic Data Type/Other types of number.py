print(int('100')) # Ép kiểu string -> int
print(int('100' , 2)) # Ép kiểu string -> từ base 2 -> 10
print(int('1ab' , 16)) # Ép kiểu string -> từ base 16 -> 10
# Lưu ý: Chỉ có thể ép kiểu string từ base 2 chứ không thể là int

# Do python phép tính 1.2 - 1.0 trong python sẽ trả về gtri 0.199999999
# -> Khá phiền phức -> Sử dụng decimals module
from decimal import Decimal, getcontext 
# In ra các class của hàm này
print(getcontext)
# Làm tròn đến số thứ tư
getcontext().prec = 4
# Phép chia 1 / 3 trả về giá trị làm tròn đến số thứ tư 
print(Decimal(1) / Decimal(3))
getcontext().prec = 2
print(Decimal(1) / Decimal(3))
print(3.14) 
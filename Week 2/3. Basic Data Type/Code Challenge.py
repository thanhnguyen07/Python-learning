# Python code​​​​​​‌‌‌​​‌‌‌​​​‌​‌‌​​‌​​​​​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
   hexNum = hexNum.upper()
   ans = 0
   cnt = 0
   for c in reversed(hexNum):
      if c not in hexNumbers:
         return None
      
      ans += hexNumbers[c] * (16 ** cnt)
      cnt += 1
   return ans

xau = "Not a number"
print(hexToDec(xau))

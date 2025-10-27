# Python code​​​​​​‌‌‌​​‌‌‌​​‌‌​​​‌​‌​‌‌‌‌​​ below

def encodeString(stringVal):
    cnt = 1
    char = stringVal[0]
    result = []

    for c in stringVal:
        if c == char:
            cnt += 1
        else:
            cnt = 1
            result.append((char , cnt))
            char = c

    result.append((char , cnt))
    return result

def decodeString(encodedList):
    s = ''

    for char , count in encodedList:
        s += char * count
    
    return s

encode_String = "AAAAABBBBAAA"
print(encodeString(encode_String))

decode_String = [('W' , 5) , ('1' , 2) , ('G' , 3)]
print(decodeString(decode_String))

# Python code​​​​​​‌‌‌​​‌‌‌‌​​​‌‌‌‌​‌‌​​‌‌‌​ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    myList = [True] * num
    myList[0] = myList[1] = False
    
    for i in range(2 , int(num ** 0.5) + 1):
        if myList[i] == True:
            for j in range(i * i , num , i):
                myList[j] = False;
    return [i for i in range(num) if myList[i]]

num = 10
print(allPrimesUpTo(num))

            

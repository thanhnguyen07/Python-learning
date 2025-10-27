# List Comprehensions
myList = [1 , 2 , 3 , 4 , 5]
print([2 * items for items in myList])

# Lists comprehensions with filters
myList = list(range(100))
filteredList = [items for items in myList if items % 10 == 0]
print(filteredList)
filteredList = [items for items in myList if items % 10 < 0]
print(filteredList)

# Lists comprehensions with functions
myString = 'My name is Ryan Mitchell. I live in Boston'
myString.split('.')
print(myString)
myString.split()
print(myString)

# Remove the dot by split function
def cleanWord(word):
    return word.replace('.', '').lower()

print(cleanWord(myString))

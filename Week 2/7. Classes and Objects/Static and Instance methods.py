# Static and Instance Methods
class WordSet:
    replacePuncs = {'!' , '.' , ',' , '\''}
    def __init__(self):
        self.words = set()
    
    def addText(self , text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(text):
        # chaining functions
        # text = text.replace('!' , '').replace(',' , '').replace('\'' , '')
        for puncs in WordSet.replacePuncs:
            text = text.replace(puncs , '')
        return text.lower()

wordSet = WordSet()

print(wordSet.addText("Hi, I\'m Ryan! Here is the sentence I want to add!"))
print(wordSet.addText("Here is another sentence I want to add."))

print(wordSet.words)

# Decorators
class WordSet:
    replacePuncs = {'!' , '.' , ',' , '\''}
    def __init__(self):
        self.words = set()
    
    def addText(self , text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    @staticmethod
    
    def cleanText(text):
        # chaining functions
        # text = text.replace('!' , '').replace(',' , '').replace('\'' , '')
        for puncs in WordSet.replacePuncs:
            text = text.replace(puncs , '')
        return text.lower()

wordSet = WordSet()

print(wordSet.addText("Hi, I\'m Ryan! Here is the sentence I want to add!"))
print(wordSet.addText("Here is another sentence I want to add."))

print(wordSet.words)
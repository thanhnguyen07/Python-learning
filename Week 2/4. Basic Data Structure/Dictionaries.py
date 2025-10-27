# Dictionary
animals = {
    'a' : 'aardvark',
    'b' : 'bear',
    'c' : 'cat',
}
print(animals['a'])
animals['d'] = 'dog'
animals['a'] = 'antelope'
print(animals)
# Lấy keys
print(animals.keys())
print(animals.values())
# Lưu ý rằng dict không thể ép kiểu về lists
# Chỉ có thể chuyển dict key thành list
print(list(animals.keys()))
# Nếu có một keys ko có trong dict mà chúng ta muốn in ký tự đó thì
print(animals.get('e' , 'elephent')) # -> Nó sẽ in ra elephant
print(len(animals))
animals = {
    'a' : ['aadverk' , 'antelope'],
    'b' : ['bear'],
}

animals['b'].append('bison')
animals['c'] = ['cat']

if 'c' not in animals:
    animals['c'] = []
animals['c'].append('cat')

#Default Dict
from collections import defaultdict
animals = defaultdict(list)
animals['e'].append('elephant')
print(animals)
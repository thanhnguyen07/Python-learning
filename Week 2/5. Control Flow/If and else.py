# If statement with "FizzBuzz"
for n in range (1 , 101):
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        if n % 3 == 0:
            print("Fizz")
        else:
            if n % 5 == 0:
                print("Buzz")
            else:
                print(n)

# Elif Statement
for n in range (1 , 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Single Line if Statement
n = 3
print("Fizz" if n % 3 == 0 else n)
fizzubzz = "Fizz" if n % 3 == 0 else n 
print("fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else n)

for n in range(1 , 101):
    print("fizzbuzz" if n % 15 == 0 else "fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else n)

print("fizzbuzz" if n % 15 == 0 else "fizz" if n % 3 == 0 else "buzz" if n % 5 == 0 else n for n in range(1 , 101))
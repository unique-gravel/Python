from decimal import DivisionByZero
from tkinter import BOTH


print("Ananya Agrawal")
print('*' * 10)

val = 10
rating = 4.9
description = False
name = "Ananya"
print(val)
print(rating)
print(description)
print(name)

name = input("What is your name : ")
color = input("What is your favourite color : ")
age = int(input("What is your age : "))
print("Hi " + name)
print(f"{name} is {age} years old.")
print(name + " likes " + color)

cat = "Ananya's cat"
cat = 'Ananya has a "cat"'
cat = "Ananya's " "cat"
cat = '''
Ananya's cat
Ananya has a "cat"
'''
print(cat)

cat = 'Ananya has a cat'
print(cat[0])
print(cat[-1])
print(cat[0:3]) ## including 0 and excluding 3
print(cat[0:])
print(cat[:5])
print(cat[:])
print(cat[1:-1]) ## second letter till second lat character
another = cat[:]
print(another)

first = 'Ananya'
last = 'Agrawal'
message = first + ' ' + last + ' is a coder'
print(message) 
msg = f'{first} {last} is a coder'
print(msg) 

name = "My name is Ananya Agrawal"
print(len(name)) 
print(name.upper())
print(name.lower())
print(name.find('n')) ## returns the first occurence
print(name.find('Ananya')) ## returns the starting index
print(name.replace('Agrawal', 'Gupta'))
print('Ananya' in name) ## finds the occurence (T/F)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 * 3)
print(10 ** 3)

# exponentiation 
# multiplication or Division
# addition or subtraction

x = 2.9
print(round(x))
print(abs(-2.9))
import math
print(math.floor(2.9))
print(math.ceil(2.9))

age = -1
if age > 0:
    print("positive integer")
elif age < 0:
    print("negative number")
else:
    print("zero")
print("Thank you :))")

is_hot = False
if is_hot:
    print("weather is hot")
else:
    print("weather is cold")
print("enjoy your day")

# and: both
# or: at least one
# not: negative

is_good = True
rain = False
if is_good and not rain:
    print("You can go outside.")
else:
    print("You cannot go outside.")

num = 5
if num >= 7 or num <= -7:
    print("It is a good number.")
else:
    print("It is not a good number")
from decimal import DivisionByZero
from tkinter import BOTH

#print
print("Ananya Agrawal")
print('*' * 10)

#variables and datatypes
val = 10
rating = 4.9
description = False
name = "Ananya"
print(val)
print(rating)
print(description)
print(name)

#input
name = input("What is your name : ")
color = input("What is your favourite color : ")
age = int(input("What is your age : "))
print("Hi " + name)
print(f"{name} is {age} years old.")
print(name + " likes " + color)

#strings
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
words = cat.split(" ")
print(words)

first = 'Ananya'
last = 'Agrawal'
message = first + ' ' + last + ' is a coder'
print(message) 
msg = f'{first} {last} is a coder'
print(msg) 

#string functions
name = "My name is Ananya Agrawal"
print(len(name)) 
print(name.upper())
print(name.lower())
print(name.find('n')) ## returns the first occurence
print(name.find('Ananya')) ## returns the starting index
print(name.replace('Agrawal', 'Gupta'))
print('Ananya' in name) ## finds the occurence (T/F)

#arithmatic operators
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

#if conditions
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

#while loops
i = 1
while i <= 5:
    print(i)
    i += 1

# patterns
i = 1
while i <= 5:
    print('*' * i)
    i += 1

i = 1
while i <= 5:
    print(' ' * (5-i), end = '')
    print('*' * i)
    i += 1

#for loops
for letter in 'Python': # iterate every element
    print(letter)

for name in ['Ananya', 'Naman', 'Harshit', 'Madhav']: #create list using []
    print(name)

for num in [1, 2, 3, 4]: #create list using []
    print(num)
 
for i in range(10): # from 0 to 9
    print(i)

for i in range(5, 10): # from 5 to 9
    print(i)

for i in range(5, 10, 2): # from 5 to 9 increment 2
    print(i)

for i in range(10, 5, -1): # from 10 to 6 decreament -1
    print(i)

for i in range(4):
    for j in range(3):
        print(f'({i}, {j})')

# PRINTING F SHAPE
numbers = [5, 2, 5, 2, 2]
for num in numbers:
    for i in range(num):
        print('X', end='')
    print(' ')

#lists - mutable
names = ['Ananya', 'Madhav', 'Harshit', 'Naman']
print(names)
print(names[1])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[:4])
print(names[:])

nums = [1, 3, 7, 5, 4, 9]
largest = 0
for num in nums:
    largest = max(num, largest)
print(largest)

#2D lists
matrix = [ [1,2,3] , [4,5,6] , [7,8,9] ]
print(matrix[0][1])

#list methods
nums = [1, 3, 7, 5, 4, 9, 3]
nums.append(20)
nums.insert(0, 10)
nums.remove(3) #remove the first oocurence
nums.pop() #removes last item
nums.index(5) # index of first occurence
print(3 in nums) #returns true or false
print(nums.count(3))
nums.sort()
nums.reverse()
nums2 = nums.copy()
nums.clear()

#tuples - immutable
nums = (1,2,3)
print(nums.count(2))
print(nums[0])

#unpacking
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
x,y,z = coordinates # assigns the respective values

#dictionaries
customer = {
    "name" : "Ananya Agrawal",
    "age" : 21,
    "item" : "bread"
}
customer["name"] = "Madhav Mishra" #change a value
customer["birthday"] = "17 Sep"#add another key
print(customer["name"])
print(customer.get("day", "!")) #print ! if not available
print(customer)

#functions
def greet_user():
    print("Hello World")
print("Start")
greet_user()
print("End")

def greet_user(name):
    print("Hello " + name)
name = input("Enter your name: ")
print("Start")
greet_user(name)
print("End")

#keyword argument
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
print("Start")
greet_user(last_name="Agrawal", first_name="Ananya")
print("End")

def area(length, bredth):
    return length*bredth
ans = area(50, 50)
print(ans)

#Exception handling
#this means instead of crashing the program, print the eception message
try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divided be zero")

#Modules
import converters
print(converters.kg_to_lbs(70))
print(converters.lbs_to_kg(70))

#packages
from ecommerce import shipping
shipping.calcShipping()

#buildin modules
import random
for i in range(3):
    print(random.randint(10,20))
    
members = ['Ananya', 'Harshit', "Naman"]
leader = random.choice(members)
print(leader)
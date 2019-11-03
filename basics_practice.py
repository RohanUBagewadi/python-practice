# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:12:15 2019

@author: rubag
"""

''' Python basics practice'''

x = 3
print(type(x)) # Prints "class of 'x' "
print(x)
print(x + 1)
print(x - 1)
print(x * 2)
print(x ** 2) # Exponential operation; Prints x^2
x += 1
print(x)
x *= 2
print(x)
y = 2.5
print(type(y)) # Prints "class of y i.e 'float' "
print(y, y + 1, y * 2, y ** 2)
print(25/4)
print(27//4) # Rounds to nearest int
print(27%4) # Reminder
print(2 ** 3) # Power of
print('{:b}'.format(21)) # Converts to binary number
print('{:o}'.format(21)) # Converts to octadecimal
print('{:x}'.format(21)) # Converts to hexadecimal

a= range(0, 10, 3) # To define range start , end, step
a = np.arange(0, 10, 3) # To to create an array start, end, step
print(a)

''' Boolean Operations'''

t = True
f = False
print(type(t)) # Prints class of 't' i.e 'float'
print(t and f) #  Logical 'AND'
print(t or f) # Logical 'OR'
print(not t) # Logical 'NOT'
print(t != f) #LOgical 'XOR'

''' Strings '''

hello = 'Hello' # Strings Literals can use single quotes
world = 'World' # or double quotes
print(type(hello))
print(len(hello))
q = 'HelloWorld'
print(q[1])
print(q[-2])
print(q[2:5])
string = 'con' + 'catenation'
print(string)
string = 2 * ('con' + 'catenation' + '-')
print(string)
print('Today I had {0} cups of {1}'.format(3, 'coffee'))
print('The prices are: {0},{1},{2}'.format(10, 20, 30))
print('The {vehicle} had {0} crashes in the year {1}'.format(2, 2005, vehicle="XYZ"))

hw = hello + world # String concatination
print(hw)
hw12 = '%s %s %d' % (hello, world, 12) #String style string formatting
print(hw12)

s = 'hello'
print(s.capitalize()) # Capitalize a string only the first letter
print(s.upper()) # convert the entire string to uppercase
print(s.rjust(7)) # Right-justifyta string i.e padding with spaces
print(s.ljust(5)) # Left-justifyta string i.e padding with spaces
print(s.center(7))  # Center a string i.e padding with spaces
print(s.replace('l', '(ell)')) # Replace all the letter of 'l' with 'ell'
print(' world '.strip()) # Removes all the whitespaces

'''Containers 
                1) Lists'''
xs = [3, 1, 2] # Creates a list
print(type(xs))
print(xs, xs[2])
print(xs[-1]) # -1 index is the last element in the list
xs[2] = 'foo' # List can contain elements of different types
print(xs)
xs.append('bar') # Adds a new element to the list
print(xs)
q = xs.pop(1) # Remove and return item at index (default last).
print(q, xs)

''' Slicing '''
nums = list(range(5)) # Range is a built in fun. that creates a sequience of numbers 
print(type(nums))
print(nums)
print(nums[2:4])
print(nums[:2])
print(nums[:])
print(nums[:-1])
print(nums[:-2]) # Assigning a new sublist to a slice
nums[2:4] = [8, 9]
print(nums)

''' Loops '''
animals = ['cat', 'dog', 'monkey']
for animals in animals:
    print(animals)

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

''' List Comprehension '''
nums = [0, 1, 2, 3, 4, 5]
square = []
for x in nums:
    print(x)
    square.append(x ** 2)
print(square)
#--OR--
squres = [x **2 for x in nums]
print(squres)
even_squres = [x ** 2 for x in nums if x % 2 == 0]
print(even_squres)


''' Dictionaries '''

d ={'cat': 'cute', 'dog': 'furry' } # Create a new dictionary with some data
print(d['cat']) # prints entry from the dictionary
print('cat' in d) # Check if the dictionary contains the given key
d['fish'] = 'wet' # Set an entry in the dictionary
print(d['fish'])
print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
del d['fish']
print(d.keys()) # prints all the keys in the dictionary
print(d.values()) # prints all the values in the dictionary
del d['cat'] # Delets the key 'cat'
d.clear() # clears the whole dictionary
new_dictionary = {x: x+1 for x in range(2,10)}
print(new_dictionary)
d = {'person':2, 'cat':4, 'spider':8}
for animal in d:
    legs = d[animal]
print('%s has %d legs' % (animals, legs))

num = [0, 1, 2, 3, 4]
even_num_to_square = {x: x **2 for x in num if x % 2 == 0 }
print(even_num_to_square)

''' Sets '''
animals = {'cat', 'dog'}
animal(1)
print(type(animals)) # Prints '<class 'set'>'
print('cat' in animals) # Chek if an element is in a set
animals.add('fish') # Adds an element to the set
print(animals)
print(len(animals)) # number of elements in the set
animals.add('dog') # Adding an element that is already present in the set does not change the lenght of the set
print(animals)
animals.remove('cat') # Removes an element in the set
print(animals)

''' Loops for set'''
animals = {'cat', 'dog', 'fish'}
for idx, animals in enumerate(animals):
    print('#%d: %s' % (idx, animals))

''' Comprehensions for set'''
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}

''' Tuples '''
d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print(type(t))
print(d[t])
print(d[(1, 2)])

''' Functions '''
def sign(x): # For degining the function def keyword is used
    if x > 0:
        return 'Positive'
    elif x < 0:
        return 'Negative'
    else:
        return 'Zero'
for x in [-1, 0, 1]:
    print(sign(x))

def hello(name, loud=False): # Function with two arguments
    if loud:
        print('Hello %s!' %  name.upper())
    else:
        print('Hey %s' % name)
hello('bob')
hello('Jim', loud=True)

''' Classes '''

class Greeter(object): # Defining the object name
    
    # Construction
    def __init__(self, name): 
        self.name = name # Creating the instane variable
    # When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance.
    
    # Instance method
    def greet(self, loud=False):
        if loud:
            print('Hello %s!' % self.name.upper())
        else:
            print('Hey %s!' % self.name)

g = Greeter('Fred') # creates a new instance of the class and assigns this object to the local variable g.
g.greet() # Calling the method 'greet' in that perticular class
g.greet(loud=True)


def fun_return():
    return 'I am me',2 # Return whatever it is specified
r = fun_return()
print(r)

def add(a, b):
    print(a + b)
q = add(10, 19)

def multiply(a, b=20):
    c = a * b
    return c
q = multiply(10)
print(q)

def division_my_2(a, b):
    
    # def even_check(a, b):
    if a % b == 0:
        return a, b
    else:
        print('Zero by error')
    c = a /b
    return c
q = division_my_2(10, 3)

def division_my_2(a, b):
    
    def even_check(a, b):
        if a % b == 0:
            c = a /b
            print(c)   
        else:
            print('Zero by error')
    even_check(a, b)
    
q = division_my_2(10, 2)

file = open('polynomial.csv', 'r') # Opens file and reald ony
print(file.read())
print(file.read(4))
file.close
print('File name:' + file.name)
print('Is file close:' + str(file.closed))
print('File mode:' + file.mode)

print(list(filter(lambda x: x+1, [1, 2, 3])))

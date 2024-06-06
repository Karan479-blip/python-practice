#input command use to take input from user
'''name=input("Enter ur name")
print("Hello,",name)'''


'''#Output statement with keyword
print("Hello","World",sep=",",end="!\n")'''



'''
#DATA TYPES IN PYTHON
int_a = 5  #use to store integer value
float_b = 2.9    #use to store float value
complex_c = 1+9j  #use to store complex value
#Numeric types (int, float, complex) are immutable

string = "Hello karan"  #use to store string value
list_f = [6,7,8,9]     #use to store list value
tuple_g = (1, 2, 3, 4, 5)    #use to store tuple value

#Sequence types (str, list, tuple) can contain multiple values of different data types


dict_h = {"name": "Karan", "age": 20}  #Mapping type store key value pairs,where keys must be unique and immutable
set_i = {1, 2, 3, 4, 5} #it is unordered collec.of unique elements


boolean = True        #use to store boolean value i.e (true/false)
'''




#EXPRESSION AND OPERATOR

#a=2
#b=3

#Arithmetic operator
'''c=a+b  # Addition
d=a-c  # subtraction
e=a*b  # multiplication
f=a/b  # division
g=a%b  # remainder
h=a**b # power
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
'''

#a=50
#b=5

# Comparison Operators
'''print(a == b) # Equal 
print(a != b) # Not equal 
print(a > b)  # Greater 
print(a < b)  # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to
'''


#a=20
#b=3
# Logical Operators
'''
c=a>5 and b<2 #True
d=a>50 and b<2 #Or
e=not(a>5 and b<2) #not
print(c)
print(d)
print(e)
'''


#TYPE CASTING

'''a= int(3.14) #int from float
b= float(5)  #float from int
c= str(20)   #string from int
d= list("Kraan")  #list from string
e= tuple([6,7,8,9])  #list from tuple
f= set([1, 2, 3, 4, 5])#set from list
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''

#CONDITIONAL STATEMENTS

'''
age = int(input("Enter your age: "))
if age >= 18:
  print("You are eligible to vote!")
elif age < 0:
  print("Invalid age. Please enter a non-negative value.")
else:
  print("You are not yet old enough to vote.")
  '''




#Looping statement

'''a=['1','2','3','4']
for i in a:
    print(i)'''


'''b=['karan','nishant','chauhan','tomar']
for i in b:
    print(i)
'''



#Jumping statement


#BREAK STETEMENT:It will terminate the statement where break statement is full fill
'''
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i == 2:
        break
    print(i)
'''
#CONTINUE:It will skip that number and print other number in series
'''
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i == 2:
        continue
    print(i)
'''
#FUNCTIONS
'''
def calculate_area(lenght, width):
  return lenght * width

area = calculate_area(3, 9)
print(area)
'''

'''
def greet(name, mass = "jelly"):
  print(mass, name + " @!")
greet(mass = "hi", name= "nish")
greet("rahul")   #jelly use for default system
'''
'''
def cal_ave(*numbers):
  if len(numbers) == 0:
    return 0
  total = sum(numbers)
  return total / len(numbers)

average = cal_ave(1, 2, 3, 4, 5)
print(average)

cal_ave()
'''


#lambda fucntions  ----------given two numbers and then uses of these two numbers
'''add = lambda x, y: x + y
result = add(3, 5)
print(result)

greeting = lambda name: f"Hello, {name}!"
print(greeting("karan"))
'''
'''
words = ["apple", "banana", "dates", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
'''


#map reduce functions
#The map function applies a given function to all elements of an iterable (like a list) and returns an iterator containing the transformed elements.
'''
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6]
'''
# Filtering even numbers using filter() and a lambda function
#even_numbers = filter(lambda x: x % 2 == 0, numbers)

# filter() also returns an iterator, convert it to a list for printing
'''print(list(even_numbers))  # Output: [2, 4, 6]

from functools import reduce

numbers = [1, 2, 3, 4, 5]
'''
# Using reduce() to find the product of all elements in the list
'''product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120

x = 10
def my_fuc():
  y = 20
  print("Inside function: ", x,y)
  def inner_fuc():
    z = 30
    print("Inside inner function: ", x,y,z)
  inner_fuc()
print("Outsider fucntion: ", x)
my_fuc()
'''
'''
#list Statistics
def analyze_list(numbers):
  if not numbers:
    return None
  average = sum(numbers) / len(numbers)
  maximum = max(numbers)
  minimum = min(numbers)
  return average, maximum, minimum
analyze_list([1,2,3,4,5])
'''

'''
#filtering and lambda
def filter_short_names(names, max_length):
  return list(filter(lambda name: len(name) <= max_length, names))
filter_short_names("nishant", 10)
'''



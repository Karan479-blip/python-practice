#Inheritance provides code reusability to the program because we can use an existing class to create a new class
'''
class Shape:
  def what_shape(self):
    print("I am a shape.")

class Square(Shape):  #the child class acquires the properties and can access all the data members and functions defined in the parent class
  pass  
square = Square()

square.what_shape() 
'''

#In this example parent class is animal by this we can see that which animal make what sound according to that we make a child class like dog make woof sound we and cat make meow so we inherit parent class in it.
'''
class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

class Poodle(Dog):  # Poodle inherits from Dog
  pass

animals = [Animal(), Dog(), Cat(), Poodle()]
for animal in animals:
  animal.make_sound()

  '''

#Single inheritance:it enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code
'''
class Animal: #Parent method
  
  def speak(self):
    print("Making animal sounds")

class Dog(Animal): #child class
my_dog = Dog()
my_dog.speak()
'''


#Multiple inheritance:  class can be derived from more than one base class
'''class Vehicle:  #parent class
  def identify(self):
    print("I am a vehicle.")

class ElectronicDevice:  #Parent class
  def identify(self):
    print("I am an electronic device.")

class ElectricCar(Vehicle, ElectronicDevice):  #Child class
  pass
my_car = ElectricCar()
my_car.identify()
'''

#Multilevel Inheritance: features of the base class and the derived class are further inherited into the new derived clas. Intermediate class is formed in this
'''
class Shape:  #Parent class
  def area(self):
    raise NotImplementedError

class Square(Shape):  #Intermediate class
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

class ColoredSquare(Square):  #Child class
  def __init__(self, side, color):
    super().__init__(side)
    self.color = color

  def describe(self):
    return f"A {self.color} square and area {self.area()}"
my_square = ColoredSquare(10, "black")
print(my_square.describe())  
'''



#Hierarchial: When more than one derived class are created from a single base
'''
class Parent:#Parent classd
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):#Child
	def func2(self):
		print("This function is in child 1.")
class Child2(Parent):#Child
	def func3(self):
		print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func2()
object2.func3()
'''



#Super Method :The super() function is used to refer to the parent class or superclass




#EXCEPTION HANDLING: exception in Python is an object that represents an error or unusual condition that has occurred during the execution of a program. It disrupts the normal flow of program execution and typically contains information about the type of error, the location where it occurred, and any relevant 


#TRY AND EXCEPT: ALLOW US TO HANDLE ERRORS

'''
x = 10
y = 0
try:
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

'''
#USING FINALLY BLOCK
'''def divide(num1, num2):
  try:
    result = num1 / num2
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  finally:
    print("Division operation attempted.")
divide(10, 2)  
divide(10, 0)
'''


#BUILT-IN EXCEPTION

#SYNTAX ERROR:A SyntaxError is raised when Python encounters code that violates the language's syntax rules. This can happen due to mistakes such as incorrect indentation, invalid syntax, or missing colons or parentheses
'''
try:
   #CODE THAT GIVING ERROR COMES IN TRY BLOCK
    if x == 5:
        print("x is equal to 5")
        # Missing colon after the if statement
except SyntaxError:
    print("SyntaxError occurred")
'''


#Indentation error:An IndentationError occurs when there is an incorrect indentation in the code. Python uses indentation to define code blocks, so proper indentation is crucial.


'''try:
    # Code with incorrect indentation
    def my_function():
        print("Inside function")
except IndentationError:
    print("IndentationError occurred")



'''


#TypeError:in this raised when an operation or function is applied to an object of an inappropriate type.
'''
try:
    # Code that performs an operation on incompatible types
    x = "hello"
    y = 5
    print(x + y)  # string and an integer
except TypeError:
    print("TypeError occurred")

'''



#VALUE ERROR :A ValueError is raised when a function receives an argument of the correct type but an inappropriate value
'''
try:
    # Code that passes an invalid value to a function
    int("hello,my name is karan")  # The string "hello" cannot be converted to an integer
except ValueError:
    print("ValueError occurred")
'''



























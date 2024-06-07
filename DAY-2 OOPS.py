class Phoneno:
  class_var = 0

  def increment(self):
    self.class_var += 1
    return self.class_var

obj = Phoneno()
obj1 = Phoneno()
print(Phoneno.class_var)
obj.increment()
print(obj.class_var)
print(obj1.class_var)

#methods in class


class Phoneno:
  def set_color(self):
    print("This is coloration of there")

onj = Phoneno()
onj.set_color()

#class methods
class abc:
  class_var = 0

  def increment(self):
    abc.class_var += 1

obj1 = abc()
obj2 = abc()

print(abc.class_var)
obj1.increment()
print(abc.class_var)
obj2.increment()
print(abc.class_var)

#static Methods: class methods that don't belong to instances of the clas
class Maths:
  @staticmethod
  def is_evenno(num):
    return num % 2 == 0

  @staticmethod
  def is_primeno(num):
    if num < 2:
      return False
    for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
        return False
    return True

print(Maths.is_evenno(2))
print(Maths.is_primeno(7))

# __init__ methods: a special method automatically called when an object is created from a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

per1 = Person("Karan", 20)
print(per1.name)
print(per1.age)

# __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


person1 = Person("Karan", 20)
print(person1)
print(str(person1))

#constructors and deconstructors
class Myclass:
  def __init__(self):
    print("Constructor called")

  def __del__(self):
    print("Destructor called")

obj = Myclass()
del obj

#methods with arguments

class MyPhoneno:
  def my_case(self, arg1, arg2):
    print(f"Arguments: {arg1}, {arg2}")

my_phone = MyPhoneno()
my_phone.my_case("Samsung", "Galaxy")

#method overloading : a technique used in object-oriented programming where multiple methods can have the same name but different parameters
class MyClass:
    def my_method(self, arg1, arg2=0):
        print(f"arg1: {arg1}, arg2: {arg2}")

obj = MyClass()
obj.my_method(10)
obj.my_method(10, 20)

class Player:

  def __init__(self, name):
    self._name = name  # Name of the player (using convention for encapsulation)

  def get_name(self):
    return self._name


player1 = Player("Karan")

print(player1.get_name())

#data abstraction
class Employee:
    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

employee = Employee("Karan", 30, 5000000)

print(employee.get_salary())

employee.set_salary(600000)
print(employee.get_salary())

#data hiding
class MyClass:
    def __init__(self):
        self.__hidden_var = 0
    def get_hidden_var(self):
        return self.__hidden_var
    def set_hidden_var(self, value):
        self.__hidden_var = value
obj = MyClass()
obj.set_hidden_var(69)
print(obj.get_hidden_var())

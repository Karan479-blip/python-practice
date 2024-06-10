#LIST METHOD

#1.append:add value at end
a= [1, 2, 3]
a.append(4)
print(a)  


#2.insert:we can insert new element
a= [1, 2, 4, 8]
a.insert(2, 3)#this insert 3 at second position
print(a)


#3.copy
original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()
original_list[2][0] = 5
print("Original list:", original_list)
print("Copied list:", copied_list)


#4.Count:number of occurence
a= [1, 2, 2, 3, 1, 4, 2]
count_num= a.count(2)
print("How many 2 in the list:",count_num)


#5.Extend:By this you can append elements from another iterable (such as another list) to the end of the current list
numbers = [1, 2, 3]
name= ["karan", "nishant"]
numbers.extend(name)
print("Numbers list after extend:", numbers)  


#6.remove:you can remove the first occurrence
a= [1, 2, 3, 2, 4]
a.remove(2)
print("List after removing 2:",a)


#7.Index: This method returns the index of the first occurrence
a= ["apple", "banana", "grapes"]
first_fruit = my_list[0]
print("First fruit:", first_fruit) 


#8.sort:sort the index of list
numbers = [3, 1, 4, 5, 2]
numbers.sort()
print("Sorted numbers (ascending):", numbers)


#9.reverse: we can reverse by using slicing
a= [1, 2, 3, 4]
reversed_list = a[::-1]
print("Original list:",a)  
print("Reversed list:", reversed_list)  
print("Original list after:",a)


#10.clear:we can remove all elements from the list
a = [10, 20, 30, "karan", "nishant"]
a.clear()
print("after clearing list:",a)



#  list of squares for numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print("List of squares:", squares)

# list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

#  list of words to uppercase
words = ["karan", "chauhan", "nishant", "tomar"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)

#TUPLE Method

a = ("apple", "banana", "cherry")
print(a)
print(len(a))
print(type(a))

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



a = ("apple", "samsumng", "blueberry", "dogyyy")
y = list(b)
y.append("oranges")
b = tuple(y)

a= ("apple", "banana", "cherry")
for x in a:
  print(x)


a = ("apple", "banana", "cherry")
b = a * 3
print(b)


#SETS
# unordered,Unchangeable,Duplicate not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#Operation in set
#union
a= {4,5,6}
b= {4,3,2}
c= a|b  
print("Union:",c)


#Intersection
a= {4,5,6}
b= {4,2,3}
c= a&b  
print("Intersection:",c)


#difference
a= {4,5,6}
b= {4,3,2}
c= a-b 
print("Difference:",c)



#METHODS in SET
#add
a= {4,5,6}
print("Before adding new value():",a)
a.add(2)
print("After adding new value():",a)


#Remove
my_set = {4,5,6}
print("Before removing the set():",a)
a.remove(4)
print("After removing the set():",a)


#POP
a= {4,5,6}
print("Before poping the set():",a)
removed_element = a.pop()
print("After poping the set():",removed_element)



#Clear
a= {4,5,6}
print("Before clearing the set():",a)
a.clear()
print("After clearing the set():",a)


#Copy
a= {4,5,6}
print("Before copying the set():",a)
copy_set = my_set.copy()
print("After copying the set():",copy_set)

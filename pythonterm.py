#name = input ("What is your name? ")
#print ("Hey " + name)
#Practice code for Q n A

#birth_year = input("Enter your birth year: ")
#age = 2081 - int(birth_year)
#print (age)

#int() :- for normal number
#x = int(1)   # x will be 1
#y = int(2.8) # y will be 2
#z = int("3") # z will be 3

#float() :- for number with decimals
#x = float(1)     # x will be 1.0
#y = float(2.8)   # y will be 2.8

#bool() :- for converting value to booleans

#str() :- for converting a value to string
#x = str("s1") # x will be 's1'
#y = str(2)    # y will be '2'
#z = str(3.0)  # z will be '3.0'

#Practice code for Num Q n A

#first = input("First: ")
#second = input("Second: ")
#sum = float(first) + float(second);
#print ("Sum: " + str(sum));

#Use of float command for sum of any number and used str for converting a value to string for addition with next string

#course = 'Python learning code'
#print (course.upper()) # To call function we need () 
#print (course.lower())
#print (course.find('a'))
#print (course.replace('rn', 'd'))
#print ('learning' in course) #for getting the boolean value

#For strings work

#temperature = 9

#if temperature > 30:
    #print("It's a hot day")
    #print("Drink plenty of water")
#elif temperature > 20:
    #print("It's a nice day")
#elif temperature > 10:
    #print("It's a bit cold")
#else:
    #print("It's cold") 
#print (temperature)

# For displaying the temperature with if's statement

#weight = float(input("Weight: ")) #we can also use int function for converting
#unit = input("(K)g or (L)bs: ")
#if unit.upper() == "K":
    #converted = (weight / 0.45)
    #print("Weight in Lbs: " + str(converted))
#else:
    #converted = (weight * 0.45)
    #print("Weight in Kgs: " + str(converted))

# For converting kg to lbs or lbs to kg and also used str int/float and so on

#s = 1
#while s <= 10:
    #print(s * 'x')
    #s = s + 1

# These are the example of while loop function

#names = ["Ram", "Shyam", "Hari", "Sushank"]
#names[3] = ("Sita")
#print (names[0:3]) #in python ram is 0, shyam is 1, hari is 2

# These are the example for making lists

#numbers = [1, 2, 4, 5]
#numbers.append(6) #To add a new element in the end we use append function
#numbers.insert(2, 3) # To add new element anywhere we use insert function and (where we wanna keep after, what we wanna keep)
#numbers.remove(3) # To remove element we use remove function
#numbers.clear() # To clear everything we use clear function
#print (3 in numbers) # Sometimes we wanna know if the given item exists or not so for that we use in operator.....It gives boolean result
#print (len(numbers)) # To know how many items are in the list we use len function

# These are the example for list method

#money = [1, 2, 3, 4, 5]
#for work in money: # This is what we do in for loop.. After for function we declare the variable and then after in operator we write the variable we already declared  
    #print(work)

#i = 0
#while i < len(money): # we can also do loop using while function but it's abit longer than for function
    #print(money[i])
    #i = i + 1

# These are the example of for loops function

#money = range(1, 10, 2) # For creating sequences we use range function (starting, ending except this value, how we want our sequence) 
#if nothing given in first then it it comes from default and that's 0

#for work in money: # Instead of money we can directly write range(1, 10, 2) we don't need to store variable seperately.
    #print (work) # For creating sequences we call out the variable that we declared after this for..That is:- work



# first = "Sushank"
# last = "Karki"
# message = first + ' [' + last + '] is a coder.'
# msg = f'{first} [{last}] is a coder.' # This is a fomatted string. we use f operator.
# print(msg)

# Example of formatted strings


# If we wanna do complex math problems then we use math module
# import math

# print(math.ceil(3.6)) # we have lots of math function
# x = 9.9
# print (round(x))
# print (abs(-9.9)) # This is the absolute function we denote it as 'abs'. This gives every value positively.


# result = "Sushank"
# a = result.lower()
# b = result.upper()
# print (b)


#numbers =  (1, 2, 3, 3)
#numbers.count(3) # These are for tuples
#fruits = ("apple", "banana", "cherry")
# mixed_tuple_example = ("Namuna", 20, 2.69)
# binit, age, gpa = mixed_tuple_example
# print("Name:", binit)
# print("Age:", age)
# print("GPA:", gpa)
#print("Mixed tuple:", mixed_tuple)

# names = ["Ram", "Sita", "Hari", "Krishna", "Binit"]
# print(names)

# for name in range(len(names) -4):
#     print("English teacher's name: ", names[name])
#     print("Nepali teacher's name: ", names[name+1])
#     print("Maths teacher's name: ", names[name+2])
#     print("Opt teacher's name: ", names[name+3])
#     print("Guffadi's name: ", names[name+4]) 



# Try it yourself or run it once and you'll know

# names = ["Ram", "Sita", "Hari", "Krishna", "Binit", "Sushank"]

#while names:  
    #print(f"Current names list: {names}")
    # names.pot(0)
    # print(f"After removing: {names}")

# This is an example of nested loop

# for x in range(5):
#     for y in range(4):
#         print(f"({x}, {y})")

# numbers = [6, 2, 4, 2, 6]

# for num in numbers:
#     print("x" * num)  # Cheat code or the easy way.
#     output = ""
#     for numb in range(num):  # To print L of x
#         output += "x"
#     print(output)




# for ten in range(5):
#     print("Hello World")





# name = input("Name: ")

# if name.lower() == "sushank":
#     password = input("Password: ")
#     if password == "1234abc":
#         age = int(input("Age: "))
#         if age == 21:
#             print ("You're Done.")
#         else:
#             print("Enter correct age")
#     else:
#         print("Password incorrect.")
# else:
#     print("Enter correct name")



# balance = 790.12
# while True:
#     try:
#         deposit = float(input("Enter the balance: "))                               # Example of try/except function
#         break
#     except ValueError:
#         print(f"Please Enter the valid amount.")             # Here I've the current balance and let the user input the value if it's true then show the sum or else call the input function until it's True.
        
# balance += deposit
# print(f"Total Balance: {balance}")


# my_list = [10, 20, 30, 40, 50]
# print(my_list[:2])                        # Output: [10, 20]

#                                                         These are the examples.
# my_list = [10, 20, 30, 40, 50]
# print(my_list[2:])                        # Output: [30, 40, 50]




# names = ["Sushank", "Binit", "Srijan"]
# for name,names in enumerate(names):                   # Example of enumerate() 
#     print(f"Roll no. {name}: {names}")                 # Adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object.


# names = ["Sushank", "Binit", "Srijan"]
# roll = [1, 3, 2]                                           # Example of zip 
#                                                            # Function combines elements from multiple iterables (lists, tuples, strings, etc.) and returns an iterator of tuples.
# for names,roll in zip(names, roll):
#     print(f"{names}'s roll num. is {roll}")



# names = ['Sushank', 'Srijan', 'Binit']
# scores = [98, 90, 69]
# for result, (name, score) in enumerate(zip(names, scores)):          # Example after combining enumerate() and zip()
#     print(f"{result}: {name} scored {score}")



# names = ['Ram', 'Hari', 'Laxman']                          # Example of list comprehension
# a = [b[0] for b in names]
# print(a)



# marks = [99, 67, 59]
# new_marks = [m+2 for m in marks]                            # In this soltion I added each marks with 2 using list comprehension method
# print(new_marks)



#### Before using list comprehension #####

# cubes = []
# for i in range(11):
#     if i % 2 == 0:
#         cubes.append(i ** 3)
# print("Cubes:", cubes)

#### After using list comprehension #####

# cubes = [x ** 3 for x in range(1, 11) if x % 2 == 0]
# print(cubes)




##### Emoji Converter ############

# message = input("-> ")
# words = message.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "                       # Used dictionaries and split() to create emoji converter
# print(output)


# def greet_user(f_name, s_name):                                        # This is paramter
#     print(f"Hi {f_name} {s_name}")
#     print("Welcome to paramter and argument lesson.")

# print("Start")
# greet_user("Sushank", "karki")  # This is argument
# print("End")
# #    OR
# print("Start")
# greet_user(s_name = "karki", f_name = "Sushank")                     # This is argument
# print("End")




# class Point:
#     def move(self):
#         print("Move")                           # These are class
    
#     def draw(self):
#         print("Draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)                                 # These are objects
# point1.draw()

# point2 = Point()
# point2.x = 10
# point2.y = 20
# print(point2.x)
# point2.move()




# a = 9861607208                                                  # Palindrome
# rev_a = str(a)[::-1]                                            # a[start:stop:step] -1 is the last words Index
# print("Reversed value:", rev_a)                                 # This is the example for reversing




# def increasing(lists):
#     n = len(lists)
#     for i in range(n):                 ####### Bubble sort ###########
#         swapped = False 
#         for j in range(0, n-i-1):
#             if lists[j] > lists[j+1]:    # checking if the j+1 is greater than j or not 
#                 lists[j], lists[j+1] = lists[j+1], lists[j]         # swapping number
#                 swapped = True          # if index 0 is greater than index 1 then it's true
#         if not swapped:            # If the number is already n sequence than it breaks
#             break
# lists = [230,47,399,10.3]
# increasing(lists)
# print(lists)

##########################################################################################



# import weight_statement           # To import different file Or  merging file
# weight_statement.weight_statement()                      # To import entire file
# #              OR
# from weight_statement import weight_statement            # To import the imp function from the file
# weight_statement()



##########################################################



# class person:
#     def __init__(self, x, y):               # Constructor attribute example
#         self.x = x
#         self.y = y
        
# people = person(20, 30)
# people.x = 21
# print(people.x)

#################################

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi I am {self.name}")    # Example of Consructor Attribute
        
        
# sushank = Person("Sushank")
# print(sushank.name)
# sushank.talk()
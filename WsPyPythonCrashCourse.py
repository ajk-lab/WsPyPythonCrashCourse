"This is my first python program"
#%%
print("Hello Python interpreter!")
print("Hello Python world!")


message = "Message: Hello Python world" #variable
print(message)



# print = "Print" # illigal to use python keyword as variable           ``
# print(print) #illigal


message_1 = 'I told my friend, "Python is my favorite language!"'
message_2 = "The language 'Python' is named after Monty Python, not the snake."
message_3 = "One of Python's strengths is its diverse and supportive community."

print(message_1)
print(message_2)
print(message_3)



name = "ajay kumar"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ajay"
last_name = "kumar"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

favorite_language_1 = '     JULIA '
print(favorite_language_1.lstrip())
print(favorite_language_1.rstrip())
print(favorite_language_1.strip())


message = "One of Python's strengths is its diverse community." 
print(message)

message = 'One of Python strengths is its diverse community.'
print(message)

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")



3*0.1

age = 23
# age must be converted to align with context
message = "Happy " + str(age) + "rd Birthday!" 
print(message)

3/2

import this
print(this)

# List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())
print(bicycles[1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 

print(bicycles[-1])


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append("ducati")
motorcycles

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

del motorcycles[0] 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")


motorcycles = ['honda', 'yamaha', 'suzuki'] 
first_owned = motorcycles.pop(0)
first_owned
motorcycles
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove("yamaha")
motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

len(cars)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles[3])


motorcycles = [] 
print(motorcycles[-1])


magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

magicians = ['alice', 'david', 'carolina'] 
print(magicians)
for magician in magicians: 
 print(magician.title() + ", that was a great trick!")

 magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")  
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")  
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
print("Thank you, everyone. That was a great magic show!")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

message = "Hello Python world!"
print(message)

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")  
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
    
    print("Thank you everyone, that was a great magic show!")

for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    sqaure = value ** 2
    squares.append(sqaure)
print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

my_foods = ['pizza', 'falafel', 'carrot cake'] 
print(my_foods)
friend_foods = my_foods
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Tuples
dimensions = (200,20)
dimensions[0]
dimensions[0] = 250
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# IF statement # Conditional Test
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
car == 'bmw'


car = 'audi'
car == 'bmw'

car = 'Audi'

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


#List #For # If
requested_toppings = ['orgegano','Mashroom']
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username1, user_info1 in users.items():
    print("\nUsername: " + username1)
    full_name = user_info1['first'] + " " + user_info1['last']
    location = user_info1['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
print(prompt)
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(int(age))

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)    


def greet_user():
    print("Hello!")
    
greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#%%
class Dog():
    """A simple attempt to model a dog.""" 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# %%
Dog('willie',6)      
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

#%%
with open(file="../WsApacheWWW/httpd.conf") as file_object_1:
    contents_1 = file_object_1.read()
    print(contents_1)

# %%
with open(file="../WsApacheWWW/httpd.conf") as file_object:
    for line in file_object:
        print(line)
# %%
with open(file="../WsApacheWWW/httpd.conf") as file_object:
    lines = file_object.readlines()
print(lines)
#%%
for line in lines:
    print(line.rstrip())
# %%
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# %%
print(5/0)
# %%
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero!")
# %%
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)

#%%
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# %%
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)   
print(numbers)
# %%
import matplotlib.pyplot as plt
squares_1 = [1, 4, 9, 16, 25]
# plt.plot(squares_1, linewidth=5)
plt.plot(squares_1)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
plt.tick_params(axis='both', labelsize=20)
plt.show()
# %%
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares_2 = [1,4,9,16,25]
plt.tick_params(axis='both',labelsize=20)
plt.plot(input_values,squares_2,linewidth=10)

# %%
import matplotlib.pyplot as plt
plt.scatter(2, 4, s=200)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
# %%
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=200)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
# %%
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
print(1001*1001)
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.axis([0,1100,0,1100000])
plt.tick_params(axis='both', labelsize=14)
plt.scatter(x_values,y_values,edgecolors='green',s=40)
plt.scatter(x_values,y_values,c='red',edgecolors='blue',s=40)
plt.scatter(x_values,y_values,c=(0.7,0.7,0.8),edgecolors='green',s=40)
# %%
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
print(1001*1001)
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=40)
# Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# plt.axis([0,1100,0,1100000])
# plt.tick_params(axis='both', labelsize=14)
# plt.scatter(x_values,y_values,edgecolors='green',s=40)
# plt.scatter(x_values,y_values,c='red',edgecolors='blue',s=40)
# plt.scatter(x_values,y_values,c=(0.7,0.7,0.8),edgecolors='green',s=40)
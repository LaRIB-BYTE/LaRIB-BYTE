p1="make a lot of money"
p2="subscribe pls"
p3="click this"
p4="buy now"

message=input("Aji apne marji ka message karo: ")


if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam message")
    
else:
    print("this is not a spam message")    
    
    
#______________________________________________ "IN" keyword ____________________________________________________    
#it serves 2 functions
#________________________________________ 1. Membership Test _____________________________________________________

# In a list
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)       # True
print('orange' in fruits)      # False

# In a string
greeting = "Hello, World!"
print('Hello' in greeting)     # True
print('Python' in greeting)    # False

# In a dictionary (checks keys by default)
person = {'name': 'Alice', 'age': 25}
print('name' in person)             # True
print('Alice' in person)            # False (checks keys, not values)

# _____________________________________________________2. Iteration in Loops____________________________________________________

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Iterating through a string
for char in greeting:
    print(char)


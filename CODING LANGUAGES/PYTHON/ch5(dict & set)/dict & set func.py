#______________________DICTIONARY_______________________________________

dict = {'name': 'Alice',
           'age': 25, 
           'city': 'New York'}

value = dict['name']                         # Accessing Values by Key

dict['age'] = 26                             # Updates the value of 'age'
dict['job'] = 'Engineer'                     # Adds a new key-value pair

del dict['city']                             # Removes the 'city' key and its associated value

keys = dict.keys()  
values = dict.values()  
items = dict.items()  

value = dict.get('city', 'Not Found')        # If 'city' does not exist, returns 'Not Found'


#_________________________________SETS__________________________________

my_set = {1, 2, 3, 4}

my_set.add(5)                                # Adds 5 to the set

my_set.remove(2)                             # Removes 2 from the set, raises KeyError if 2 is not present

my_set.discard(10)                           # No error if 10 is not in the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  

intersection_set = set1.intersection(set2)  

difference_set = set1.difference(set2)  

if 2 in my_set:
    print("2 is in the set")

my_set.clear()                             # Empties the set

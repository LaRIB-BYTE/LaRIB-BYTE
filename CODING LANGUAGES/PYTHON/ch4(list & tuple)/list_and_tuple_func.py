
#___________________________________________LIST_________________________________________________________________________________________

list = [1,3,4,"harry",2.3,4]  #List is ordered, indexed, mutable and most flexible and dynamic collection of elements in python.
index_3 = list.index(4)
print(index_3)                #list.index() -it tells us the index position of the element we entered

list2=[1,3,4,"harry",2.3,4]
list2.insert(6,"king")
print(list2)                  #list.insert() - inserts value at given position


list3=[1,2,3,"harry",4.5,5]
list3.reverse()            
print(list3)                   #list.reverse() - reverse the list can also be done by slicing


list3_2=[1,2,3,"harry",4.5,5]  #by silcing
rev_list3_2=list3_2[::-1]
print(rev_list3_2)

list4=["zebra","hen","cock","goat"]  #list,pop() - Removes and returns the item at the specified index (or the last item if no index is specified)
print(list4.pop(2))

#len,sum,min,max,sorted some common func. of list to manipulate it
my_list=[100,20,80,29,39,99,293,999]
length = len(my_list)
print(length)

total = sum(my_list)
print(total)

smallest = min(my_list)
print(smallest)

largest = max(my_list)
print(largest)

sorted_list = sorted(my_list)
print(sorted_list)


#_______________________________________________TUPLE_____________________________________________________________________

'''A tuple is a built-in data type in Python that is similar to a list, but with two key differences:
1.Immutability: Once a tuple is created, its contents cannot be changed (you can't add, remove, or modify elements).
2.Syntax: Tuples are defined using parentheses () instead of square brackets [].'''

my_tuple = (1, 2, 3)

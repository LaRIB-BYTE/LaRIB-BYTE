

''' string[start:stop:step] '''

text = "Hello, World!"

substring = text[0:5]
print(substring)

#step wala slicing
substring_with_step = text[0:5:2]          #Explanation: It starts at index 0, goes up to index 5, but takes every second character due to the step of 2.
print(substring_with_step)

naam= "kachde ki dukaan"
print(naam[0:10:2])

# From the start to index 5
print(text[:5])  

# From index 7 to the end
print(text[7:]) 


# Last 6 characters
print(text[-6:]) 

# Slice with negative step (reverse string)
print(text[::-1])  




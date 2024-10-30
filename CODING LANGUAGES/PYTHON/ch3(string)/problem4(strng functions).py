jindal = "larib will see the light  of the sun"    #string.replace
print(jindal.replace("  "," "))
print(jindal.replace("will","will never"))

tex1 = "Hello, World!"                             #len()
length = len(tex1)
print(length)  

text2 = "HELLO, WORLD!"                            #strng.lower()   &  #string.upper()
lowercase = text2.lower()
print(lowercase)  

text3 = "   Hello, World!   "                      #strng.strip() - removes white space from start to trail
stripped = text3.strip()
print(stripped)  

text4 = "Hello, World!"                            #strng.split(sep) - Splits the string into a list of substrings based on a specified separator.
words = text4.split(", ")                          # string to list
print(words)  

set = ['Hello', 'World','king']                    # .join(iterable) - Joins elements of an iterable (like a list) into a single string, using the string as a separator
joined = " & ".join(set)                           # list to string
print(joined)  
print(type(set))

s = "12345"                                        # .isdigit() - Returns True if all characters in the string are digits.
print(s.isdigit())                                 

s = "Hello"                                        # .isalpha() - returns True if all characters in the string are alphabetic (letters only).
print(s.isalpha())                                  

s = "Hello123"                                     # .isalnum() - Returns True if all characters are alphanumeric (letters and numbers).
print(s.isalnum())                                 

s = "   "                                          # .isspace() - returns True if the string contains only whitespace characters (spaces, tabs, etc.).
print(s.isspace())  

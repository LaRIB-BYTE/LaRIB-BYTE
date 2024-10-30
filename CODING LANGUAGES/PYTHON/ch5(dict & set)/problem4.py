s=set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

#it shows only 2 lenth becuz 20 and 20.0 are considered equal in python thats why set only stores 2 values

print(s)
#to find the factorial of a number
# 5! = 5 x 4 x 3 x 2 x 1

n=int(input("Enter a number: "))
product=1
for i in range(1,n+1):
    product = product * i
    
print(f"The factorial of {n} is {product}")    
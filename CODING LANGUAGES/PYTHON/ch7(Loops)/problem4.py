#to check if a given number is prime or not

n=int(input("enter a number: "))

for i in range(2,n):
    if(n%i)==0:
        print("This is not a prime number")
        break
         
else:
    print("this is a prime number")    
#for a pattern of where n = 3

n=int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")         #end= is used because puthon automtacilly starts a new line after 1 print
    print("*"* (2*i-1), end="")
    print("")
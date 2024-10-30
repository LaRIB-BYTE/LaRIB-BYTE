#multiplication table

n=int(input("enter a number: "))

for i in range(1,11):                              #range(start,stop,step_size) {sarts} 1 se jo bhi last number hai uska {stops} -1 tak jana hoga
    print(f"{n} X {i} = {n * i}")
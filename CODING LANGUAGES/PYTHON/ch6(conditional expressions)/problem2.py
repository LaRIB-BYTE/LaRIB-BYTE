marks1=int(input("Enter the marks 1: "))
marks2=int(input("Enter the marks 2: "))
marks3=int(input("Enter the marks 3: "))

#total percentage in all subjects combined
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=100):
    print("munde highest aye hai") 
    print(total_percentage)

elif(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("congratulations u have passed succesfully")
    print(total_percentage)

else:
    print("u have failed munde jii")
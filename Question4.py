def calculate_of_power(x,y):
    if y==0:
        return 1
    else:
        return(x*calculate_of_power(x,y-1))
num=int(input("Enter number:\n"))
pow=int(input("Enter the power:\n"))
print("After Calculating Power:")
print(calculate_of_power(num,pow))
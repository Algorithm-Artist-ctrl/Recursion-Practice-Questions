def sum_of_digit(digit):
    if digit==0:
        return 0
    else:
        sum=digit%10+sum_of_digit(digit//10)
        return sum
num=int(input("Input the digit:\n"))
print(sum_of_digit(num))
def count_of_digit(digit):
    if digit==0:
        return 0
    else:
        return 1+count_of_digit(digit//10)
num=int(input("Enter digit:\n"))
print(count_of_digit(num))
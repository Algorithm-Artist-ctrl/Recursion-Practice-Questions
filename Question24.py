def sum(num):
    if num<10:
        return num
    sum_of_digit =num%10+sum(num//10)
    return sum(sum_of_digit)
print(sum(38))
'''
3+8=11
then 1+1=2 
'''
def sum_of_list(lst, x):
    if x == 0:
        return 0
    else:
        return lst[x - 1] +sum_of_list(lst, x - 1)

usr_input = input("Input numbers separated by space:\n")
usr_lst = list(map(int, usr_input.split()))
print("Sum:", sum_of_list(usr_lst, len(usr_lst)))

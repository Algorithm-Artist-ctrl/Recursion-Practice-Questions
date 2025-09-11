def print_all_indices(l1, k, ind):
    if ind == len(l1):
        return
    if l1[ind] == k:
        print(ind)
    print_all_indices(l1, k, ind + 1)

l = [10, 20, 10, 30, 10]
print_all_indices(l, 10, 0)

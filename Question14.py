def sumArray(l1):
    if len(l1)==0:
        return 0
    ans=l1[0]+sumArray(l1[1:])
    return ans
print(sumArray([1,2,3,4,5,6,7,8]))
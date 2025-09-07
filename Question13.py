"Check if array or list is sorted ?"
def checksorted(l1):
    if (len(l1)==0 or len(l1)==1):
        return True
    if (l1[0]<l1[1]):
        return checksorted(l1[1:])
    else:
        return False
l2=[i for i in range(1,10)]
print(checksorted(l2))
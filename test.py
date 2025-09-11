def binarySearch(l,k):
    if len(l)==0:
        return False
    else:
        mid=len(l)//2
        if l[mid]==k:
            return  True
        elif l[mid]<k:
            return binarySearch(l[mid+1:],k)
        else:
            return binarySearch(l[:mid],k)
l=[10,20,30,10,20]
l.sort()
print(binarySearch(l,10))
    
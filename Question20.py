def linearSearch(l,k,ind):
    if ind==len(l):
        return False
    elif l[ind]==k:
        return True
    else:
        return linearSearch(l,k,ind+1)
n=60
print(linearSearch([10,20,10,30],n,0))
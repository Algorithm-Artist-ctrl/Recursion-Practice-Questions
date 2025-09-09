def  index(l1,x):
    if len(l1)==0:
        return -1
    if (l1[0]==x):
        return 0
    ans=index(l1[1:],x)
    if ans==-1:
        return ans
    else:
        return ans+1
print(index([2,1,4,5,6,7],4))
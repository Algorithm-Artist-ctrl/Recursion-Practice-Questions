def reversestring(s,n):
    if n==0:
        print(s[0])
    else:
        print(s[n],end='')
        reversestring(s,n-1)
string=input("Enter String:\n")
print("Arter Reversing we get:")
reversestring(string,len(string)-1)

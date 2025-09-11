def palindrome(s):
    if len(s) <= 1:
        print("Palindrome")
    if s[0] == s[-1]:
        palindrome(s[1:-1])
    else:
        print("Not a palindrome")
palindrome("hello")

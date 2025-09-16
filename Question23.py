class Solution(object):
    def isPalindrome(self, s):
        def palindrome(s, start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return palindrome(s, start + 1, end - 1)

        return palindrome(s, 0, len(s) - 1)
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  

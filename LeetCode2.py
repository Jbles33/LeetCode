class Solution:
    def isPalindrome(self, x: int) -> bool:

        y = str(x)
        if y == y[::-1]:
            return True
        elif y != y[::-1]:
            return False




s = Solution()
print(s.isPalindrome(121))
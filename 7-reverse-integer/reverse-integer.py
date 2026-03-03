class Solution:
    def reverse(self, x):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        rev = sign * rev
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        
        return rev
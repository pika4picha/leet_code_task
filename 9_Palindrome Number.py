# Runtime 78ms
# Memory 16.37 Mb
# Решение задачи 9.Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        i = 0
        j = len(str_num) - 1
        while i <= j:
            if(str_num[i] != str_num[j]):
                return False
            i+=1
            j-=1
        return True

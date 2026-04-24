class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        
        check_1 = []
        check_2 = []

        for num in reversed(x_str):
            check_1.append(num) 
        
        for num in x_str:
            check_2.append(num)

        if check_1 == check_2:
            return True
        return False
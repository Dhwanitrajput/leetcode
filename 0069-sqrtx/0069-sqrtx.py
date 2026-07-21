class Solution:
    def mySqrt(self, x):
        odd = 1
        n = 0

        while(x > 0):
            x -= odd
            odd += 2
            n +=1

        if(x == 0):
            return n

        return n - 1


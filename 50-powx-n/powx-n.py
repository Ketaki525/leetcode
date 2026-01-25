class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            if n==0 :
                return 1
        
            if n==1:
                return x
        
            res = rec(x,n//2)
            if n % 2 == 0:
                return res * res
            return x * res * res

        if n < 0:
            return 1 / rec(x,abs(n))
        return rec(x,n)

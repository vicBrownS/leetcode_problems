"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= x^n <= 10^4
"""
class Solution(object):
    def myPow(self, x, n):
        """
        Computes x raised to the power n (x^n) using fast exponentiation.

        Args:
            x (float): The base number.
            n (int): The exponent (can be negative).

        Returns:
            float: The result of x raised to the power n.

        This implementation uses a recursive divide-and-conquer strategy
        to reduce the time complexity from O(n) to O(log n).
        """
        if n < 0:
            x = 1 / x
            n = -n

        def fast_pow(x, n):
            if n == 0:
                return 1
            half = fast_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return fast_pow(x, n)





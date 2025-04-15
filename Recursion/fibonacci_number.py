"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Constraints:

0 <= n <= 30
"""
class Solution(object):
    def fib(self, n):
        """
        Computes the n-th Fibonacci number using recursion with memoization.

        Args:
            n (int): The index of the Fibonacci number to compute (0-indexed).

        Returns:
            int: The n-th Fibonacci number.

        This approach uses a top-down recursive strategy with memoization
        to avoid redundant computations, giving linear time complexity.
        """
        cache = {}

        def recur_fib(n):
            if n in cache:
                return cache[n]
            if n < 2:
                cache[n] = n
            else:
                cache[n] = recur_fib(n - 1) + recur_fib(n - 2)
            return cache[n]

        return recur_fib(n)

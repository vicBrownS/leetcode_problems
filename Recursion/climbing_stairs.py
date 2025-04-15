"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:

1 <= n <= 45
"""
class Solution(object):
    def climbStairs(self, n):
        """
        Computes the number of distinct ways to climb to the top of a staircase with `n` steps,
        where at each step you can climb either 1 or 2 stairs.

        Args:
            n (int): The total number of steps.

        Returns:
            int: The number of distinct ways to reach the top.

        This solution uses top-down recursion with memoization (caching)
        to avoid redundant subproblems, similar to computing Fibonacci numbers.
        """
        cache = {}

        def stairs_recursive(n):
            if n in cache:
                return cache[n]
            if n <= 2:
                cache[n] = n
            else:
                cache[n] = stairs_recursive(n - 1) + stairs_recursive(n - 2)
            return cache[n]

        return stairs_recursive(n)



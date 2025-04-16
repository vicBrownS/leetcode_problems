"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        Dado un array de enteros `nums`, devuelve el índice de pivote,
        es decir, el primer índice tal que la suma de los elementos a la izquierda
        es igual a la suma de los elementos a la derecha.

        Si no existe tal índice, devuelve -1.

        Ejemplo:
        Input: [1, 7, 3, 6, 5, 6]
        Output: 3 (porque 1+7+3 = 11 y 5+6 = 11)

        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)  # Suma total del array
        left_sum = 0        # Inicializamos la suma izquierda

        for i in range(len(nums)):
            # La suma derecha es el total menos lo que hay a la izquierda y el elemento actual
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i  # Encontramos el índice de pivote

            left_sum += nums[i]  # Acumulamos el valor actual en la suma izquierda

        return -1  # No se encontró ningún índice que cumpla la condición


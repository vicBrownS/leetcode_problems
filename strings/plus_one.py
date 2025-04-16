"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        Dado un número representado como un array de dígitos (sin ceros a la izquierda),
        incrementa el número en una unidad y devuelve el array resultante.

        Ejemplo:
        Input: [1, 2, 3]
        Output: [1, 2, 4]

        Maneja correctamente los acarreos, por ejemplo:
        Input: [9, 9, 9]
        Output: [1, 0, 0, 0]

        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # Sumamos uno al dígito actual

            if digits[i] > 9:
                digits[i] = 0  # Si hay acarreo, ponemos a 0 y seguimos
            else:
                return digits  # Si no hay acarreo, terminamos aquí

        # Si hemos salido del bucle, todos eran 9s → se añade un 1 al principio
        return [1] + digits


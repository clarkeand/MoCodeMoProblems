class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle the edge cases explicitly
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        if divisor == 0:
            return float('inf') if dividend >= 0 else float('-inf')

        # Store the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert the dividend and divisor to positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            # Find the largest multiple of divisor that fits into the remaining dividend
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the multiple of divisor from the dividend
            dividend -= temp
            quotient += multiple

        return sign * quotient

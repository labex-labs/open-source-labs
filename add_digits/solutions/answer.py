class Solution(object):

    def add_digits(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        digits_sum = sum(digits)
        if digits_sum >= 10:
            return self.add_digits(digits_sum)
        else:
            return digits_sum

    def add_digits_optimized(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 0:
            raise ValueError('num cannot be negative')
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

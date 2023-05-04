import math


class Math(object):
    def check_prime(self, num):
        if num is None:
            raise TypeError("num cannot be None")
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def check_prime_optimized(self, num):
        if num is None:
            raise TypeError("num cannot be None")
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

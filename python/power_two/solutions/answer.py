class Solution(object):

    def is_power_of_two(self, n):
        if n is None:
            raise TypeError('n cannot be None')
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

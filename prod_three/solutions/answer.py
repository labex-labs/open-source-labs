class Solution(object):

    def max_prod_three_nlogn(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if len(array) < 3:
            raise ValueError('array must have 3 or more ints')
        array.sort()
        product = 1
        for item in array[-3:]:
            product *= item
        return product

    def max_prod_three(self, array):
        if array is None:
            raise TypeError('array cannot be None')
        if len(array) < 3:
            raise ValueError('array must have 3 or more ints')
        curr_max_prod_three = array[0] * array[1] * array[2]
        max_prod_two = array[0] * array[1]
        min_prod_two = array[0] * array[1]
        max_num = max(array[0], array[1])
        min_num = min(array[0], array[1])
        for i in range(2, len(array)):
            curr_max_prod_three = max(curr_max_prod_three,
                                      max_prod_two * array[i],
                                      min_prod_two * array[i])
            max_prod_two = max(max_prod_two,
                               max_num * array[i],
                               min_num * array[i])
            min_prod_two = min(min_prod_two,
                               max_num * array[i],
                               min_num * array[i])
            max_num = max(max_num, array[i])
            min_num = min(min_num, array[i])
        return curr_max_prod_three

from bitstring import BitArray  # Run pip install bitstring


class Bits(object):

    def new_int(self, array, max_size):
        if not array:
            raise TypeError('array cannot be None or empty')
        bit_vector = BitArray(max_size)
        for item in array:
            bit_vector[item] = True
        for index, item in enumerate(bit_vector):
            if not item:
                return index
        return None

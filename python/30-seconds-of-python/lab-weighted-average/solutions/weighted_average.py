def weighted_average(nums, weights):
    return sum(x * y for x, y in zip(nums, weights)) / sum(weights)

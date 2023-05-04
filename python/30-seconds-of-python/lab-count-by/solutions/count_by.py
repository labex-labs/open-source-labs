from collections import defaultdict


def count_by(lst, fn=lambda x: x):
    count = defaultdict(int)
    for val in map(fn, lst):
        count[val] += 1
    return dict(count)

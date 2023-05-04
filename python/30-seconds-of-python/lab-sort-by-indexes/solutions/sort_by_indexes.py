def sort_by_indexes(lst, indexes, reverse=False):
    return [
        val
        for (_, val) in sorted(zip(indexes, lst), key=lambda x: x[0], reverse=reverse)
    ]

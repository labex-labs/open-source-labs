def unfold(fn, seed):
    def fn_generator(val):
        while True:
            val = fn(val[1])
            if val == False:
                break
            yield val[0]
        pass

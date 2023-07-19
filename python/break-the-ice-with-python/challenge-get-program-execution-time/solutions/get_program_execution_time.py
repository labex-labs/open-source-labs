import time


def get_program_execution_time():
    before = time.time()
    for i in range(10000000):
        x = 1 + 1
    after = time.time()
    execution_time = after - before
    print(execution_time)


get_program_execution_time()

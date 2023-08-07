# Step 1 Solution

# logcall.py

from functools import wraps


def logged(func):
    print("Adding logging to", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper

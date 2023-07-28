# Step 2 Solution

# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
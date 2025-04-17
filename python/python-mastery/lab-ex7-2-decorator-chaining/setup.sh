#!/bin/zsh

# Download and set up the Python shell history script
cd /tmp && wget https://cdn.jsdelivr.net/gh/labex-labs/common-scripts@master/python-shell-history/.setup-python-shell-history.sh && zsh .setup-python-shell-history.sh

# Create initial files with starter code
cat > /home/labex/project/logcall.py << 'EOL'
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
EOL

cat > /home/labex/project/validate.py << 'EOL'
class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')
        
        # Run the function and get the result
        result = func(*args, **kwargs)
        
        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')
        
        return result
    return wrapper
EOL

cat > /home/labex/project/sample.py << 'EOL'
from logcall import logged

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y
EOL

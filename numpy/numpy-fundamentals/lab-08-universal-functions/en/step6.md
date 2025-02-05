# Overriding Ufunc Behavior

Classes, including ndarray subclasses, can override how ufuncs act on them by defining certain special methods. This allows for customization of ufunc behavior. Let's see an example.

```python
import numpy as np

# Define a custom class
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# Create an instance of the custom class
arr = MyArray([1, 2, 3])

# Perform addition
result = arr + 1

# Print the result
print(result)
```

Output:

```
Custom add method called
[2 3 4]
```

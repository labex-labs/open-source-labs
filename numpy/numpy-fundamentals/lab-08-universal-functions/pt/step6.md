# Substituindo o Comportamento de _Ufuncs_

Classes, incluindo subclasses de _ndarray_, podem substituir como as _ufuncs_ agem sobre elas, definindo certos métodos especiais. Isso permite a personalização do comportamento das _ufuncs_. Vamos ver um exemplo.

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

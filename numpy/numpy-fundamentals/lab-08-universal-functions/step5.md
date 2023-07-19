# Type Casting Rules

Type casting is done on the inputs of a ufunc when there is no core loop implementation for the input types provided. The casting rules determine when a data type can be safely cast to another data type. Let's see an example.

```python
import numpy as np

# Check if int can be safely cast to float
result = np.can_cast(np.int, np.float)

# Print the result
print(result)
```

Output:

```
True
```

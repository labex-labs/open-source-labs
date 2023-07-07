# Broadcasting Examples

Let's look at some examples to understand how broadcasting works in different scenarios.

- Example 1:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

In this case, `b` is added to each row of `a`. The result is a 2D array with the same shape as `a`, where each element is the sum of the corresponding elements in `a` and `b`.

- Example 2:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

In this case, broadcasting fails because the trailing dimensions of `a` and `b` are not equal. It is impossible to align the values in the rows of `a` with the elements of `b` for element-wise addition.

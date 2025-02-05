# Broadcasting with a Scalar Value

Broadcasting also allows for element-wise operations between an array and a scalar value. The scalar value is automatically "stretched" to match the shape of the array. For example:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
result = a * b
```

In this case, `b` is a scalar value, but it is stretched to become an array with the same shape as `a`. The multiplication is then done element-wise, resulting in `[2.0, 4.0, 6.0]`.

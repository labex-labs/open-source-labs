# Broadcasting with Arrays of the Same Shape

In the simplest case, two arrays must have exactly the same shape for element-wise operations. For example:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
result = a * b
```

In this case, `a` and `b` have the same shape, so the multiplication is done element-wise and the result is `[2.0, 4.0, 6.0]`.

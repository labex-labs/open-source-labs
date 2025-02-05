# Practical Example - Vector Quantization

Let's explore a practical example where broadcasting is useful. Consider the vector quantization (VQ) algorithm used in information theory and classification. The basic operation in VQ is to find the closest point in a set of points to a given point. This can be done using broadcasting. Here's an example:

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

In this example, `observation` represents the weight and height of an athlete to be classified, and `codes` represents different classes of athletes. By subtracting `observation` from `codes`, broadcasting is used to calculate the distance between `observation` and each of the codes. The `argmin` function is then used to find the index of the closest code.

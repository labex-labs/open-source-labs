# Generate Sample Data

First, we generate a sample dataset consisting of 40 random values between 0 and 5. We then compute the sine function of each value and add some noise to every 5th value.

```python
import numpy as np

# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
```



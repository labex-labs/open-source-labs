# Create sample data

Next, we need to create some sample data to fit our isotonic regression model. In this example, we will generate two arrays, `X` and `y`, representing the input data and the target values, respectively.

```python
import numpy as np

# Generate random input data
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```

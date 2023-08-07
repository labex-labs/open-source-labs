# Create test data

First, we will create some test data to use for the violin plot. We will use NumPy to generate four arrays of 100 normally distributed values with increasing standard deviations.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```

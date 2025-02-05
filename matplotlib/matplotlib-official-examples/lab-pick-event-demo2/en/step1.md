# Generate Random Data

First, we need to generate 100 random datasets, each containing 1000 random numbers between 0 and 1. We will use numpy's random module to generate the random data.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```

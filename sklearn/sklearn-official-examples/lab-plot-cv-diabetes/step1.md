# Load and prepare the dataset

First, we will load and prepare the diabetes dataset. We will only use the first 150 samples for this exercise.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```



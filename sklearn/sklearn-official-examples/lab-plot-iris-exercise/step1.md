# Load the Data

We will start by loading the Iris dataset and selecting only the first two features for visualization purposes.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]
```



# Load the Dataset

First, we need to load the Iris dataset using scikit-learn's built-in `load_iris()` function.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```

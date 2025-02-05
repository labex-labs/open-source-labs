# Load the dataset and generate random features

We will use the iris dataset, which consists of measurements taken from 3 types of irises, and generate some random feature data (i.e., 20 features), uncorrelated with the class labels in the iris dataset.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```

# Generate Data

The first step is to generate some example data that we can use to train and test our model. We will use the `make_classification` function from the `sklearn.datasets` module to generate a random binary classification problem with 3 informative features.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```



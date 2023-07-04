# Estimator Objects

Estimator objects in scikit-learn are used to learn from data and make predictions. They can be classification, regression, or clustering algorithms, or transformers that extract useful features from raw data. Let's create a simple example of an estimator object:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Implementation of the fit method
        pass

estimator = Estimator()
```

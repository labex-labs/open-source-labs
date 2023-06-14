# Data Preparation

First, we will create a large dataset of 80,000 samples and split it into three sets:

- A set to train the ensemble methods which are later used to as a feature engineering transformer
- A set to train the linear model
- A set to test the linear model.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```



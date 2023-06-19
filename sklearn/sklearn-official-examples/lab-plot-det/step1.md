# Generate Synthetic Data

We will use scikit-learn's `make_classification` function to generate synthetic data. This function generates a random n-class classification problem, with n_informative informative features, n_redundant redundant features, and n_clusters_per_class clusters per class. We will generate 1000 samples with 2 informative features and a random state of 1. We will then split the data into training and test sets with a 60/40 ratio.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```



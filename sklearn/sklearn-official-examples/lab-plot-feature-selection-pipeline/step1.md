# Generate and Split the Dataset

We will start by generating a binary classification dataset using Scikit-learn's `make_classification` function. We will also split the dataset into training and testing subsets using Scikit-learn's `train_test_split` function.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```

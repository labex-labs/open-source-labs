# Data generation

We will generate a classification task using scikit-learn's `make_classification` function. We will generate 500 samples with 15 features, out of which 3 are informative, 2 are redundant, and 10 are non-informative.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```



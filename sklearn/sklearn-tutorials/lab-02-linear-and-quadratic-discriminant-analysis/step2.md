# Generate synthetic data

Next, we will generate synthetic data to demonstrate the difference between LDA and QDA. We will use the `make_classification` function from scikit-learn to create two classes with distinct patterns.

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```

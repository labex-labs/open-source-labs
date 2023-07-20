# Univariate feature selection

Univariate feature selection works by selecting the best features based on univariate statistical tests. In scikit-learn, there are several classes that implement univariate feature selection:

- `SelectKBest`: selects the top k highest scoring features
- `SelectPercentile`: selects a user-specified percentage of highest scoring features
- `SelectFpr`: selects features based on the false positive rate
- `SelectFdr`: selects features based on the false discovery rate
- `SelectFwe`: selects features based on family wise error
- `GenericUnivariateSelect`: allows selection with a configurable strategy

Here is an example of using `SelectKBest` to select the two best features from the Iris dataset:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Initialize SelectKBest with the f_classif scoring function and k=2
selector = SelectKBest(f_classif, k=2)

# Select the best features
X_selected = selector.fit_transform(X, y)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", selector.get_support(indices=True))
```

In this example, we use the `f_classif` scoring function and select the two best features from the Iris dataset. The output will show the original shape of the dataset and the shape after selecting the best features.

# Univariate Feature Selection

Next, we will perform univariate feature selection with F-test for feature scoring. We will use the default selection function to select the four most significant features.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```



# Native Support for Categorical Features in HistGradientBoosting Estimators

`HistGradientBoostingClassifier` and `HistGradientBoostingRegressor` now have native support for categorical features. They can consider splits on non-ordered, categorical data. In this step, we will explore the new `categorical_features` parameter.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import HistGradientBoostingClassifier

# load the breast cancer dataset
data = load_breast_cancer()

# create the classifier
clf = HistGradientBoostingClassifier(
    max_iter=100, learning_rate=0.1, max_depth=3, random_state=0
)

# specify the categorical features
cat_features = [False] * data.data.shape[1]
cat_features[3] = True
cat_features[5] = True

# fit the model
clf.fit(data.data, data.target, categorical_features=cat_features)
```



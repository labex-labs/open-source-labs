# Native support for missing values for gradient boosting

The HistGradientBoostingClassifier and HistGradientBoostingRegressor now have native support for missing values (NaNs). This means that there is no need for imputing data when training or predicting.

```python
from sklearn.ensemble import HistGradientBoostingClassifier

X = np.array([0, 1, 2, np.nan]).reshape(-1, 1)
y = [0, 0, 1, 1]

gbdt = HistGradientBoostingClassifier(min_samples_leaf=1).fit(X, y)
print(gbdt.predict(X))
```



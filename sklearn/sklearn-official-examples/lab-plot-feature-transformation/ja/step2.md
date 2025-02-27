# アンサンブル手法の学習

各アンサンブル手法について、推定器を10個、最大深さを3段階に設定します。

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

n_estimators = 10
max_depth = 3

random_forest = RandomForestClassifier(
    n_estimators=n_estimators, max_depth=max_depth, random_state=10
)
random_forest.fit(X_train_ensemble, y_train_ensemble)

gradient_boosting = GradientBoostingClassifier(
    n_estimators=n_estimators, max_depth=max_depth, random_state=10
)
_ = gradient_boosting.fit(X_train_ensemble, y_train_ensemble)
```

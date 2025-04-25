# 训练集成方法

对于每种集成方法，我们将使用 10 个估计器，最大深度为 3 层。

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

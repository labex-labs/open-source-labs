# 使用离散 SAMME 和真实 SAMME.R 的 Adaboost

我们现在定义离散和真实的 AdaBoost 分类器，并将它们拟合到训练集上。

```python
from sklearn.ensemble import AdaBoostClassifier

ada_discrete = AdaBoostClassifier(
    estimator=dt_stump,
    learning_rate=learning_rate,
    n_estimators=n_estimators,
    algorithm="SAMME",
)
ada_discrete.fit(X_train, y_train)

ada_real = AdaBoostClassifier(
    estimator=dt_stump,
    learning_rate=learning_rate,
    n_estimators=n_estimators,
    algorithm="SAMME.R",
)
ada_real.fit(X_train, y_train)
```

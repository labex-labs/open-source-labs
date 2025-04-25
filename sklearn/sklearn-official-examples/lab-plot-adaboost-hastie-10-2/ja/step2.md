# 離散的な SAMME と実際の SAMME.R を使った Adaboost

次に、離散的な Adaboost 分類器と実際の Adaboost 分類器を定義し、訓練セットに適合させます。

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

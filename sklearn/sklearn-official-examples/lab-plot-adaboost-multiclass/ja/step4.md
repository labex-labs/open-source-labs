# モデルを作成して訓練する

SAMME を使用する AdaBoost モデルと SAMME.R を使用する AdaBoost モデルの 2 つを作成します。両方のモデルは、最大深さが 2 で推定器が 300 個の DecisionTreeClassifier を使用します。

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```

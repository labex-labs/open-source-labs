# モデルを作成して訓練する

SAMMEを使用するAdaBoostモデルとSAMME.Rを使用するAdaBoostモデルの2つを作成します。両方のモデルは、最大深さが2で推定器が300個のDecisionTreeClassifierを使用します。

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

# グリッドサーチを実行する

このステップでは、GridSearchCV 関数を使ってグリッドサーチを実行します。DecisionTreeClassifier モデルの min_samples_split パラメータの最適なハイパーパラメータを検索します。

```python
gs = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"min_samples_split": range(2, 403, 20)},
    scoring=scoring,
    refit="AUC",
    n_jobs=2,
    return_train_score=True,
)
gs.fit(X, y)
results = gs.cv_results_
```

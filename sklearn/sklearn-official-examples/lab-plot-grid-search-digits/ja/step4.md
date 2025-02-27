# モデルの適合と予測の実行

モデルを適合させ、評価セットに対して予測を行います。

```python
grid_search.fit(X_train, y_train)

# グリッドサーチにより、私たちのカスタム戦略で選択されたパラメータは：
grid_search.best_params_

# 最後に、残された評価セットで微調整されたモデルを評価します：
# `grid_search` オブジェクトは、私たちのカスタム再学習戦略によって選択されたパラメータを使って、完全な学習セットで **自動的に再学習されています**。
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```

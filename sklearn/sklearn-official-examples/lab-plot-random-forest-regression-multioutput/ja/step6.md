# 新しいデータに対する予測

テストデータに対する予測を行うために、ランダムフォレスト回帰器と多次元出力回帰器の両方を使用します。

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```

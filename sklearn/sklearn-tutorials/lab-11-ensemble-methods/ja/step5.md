# バギング分類器 (Bagging Classifier) の評価

`score` メソッドを使用してテストデータの正解率 (accuracy score) を計算することで、バギング分類器 (Bagging Classifier) を評価しましょう。

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```

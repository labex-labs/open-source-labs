# ランダムフォレスト分類器 (Random Forest Classifier) の評価

テストデータの正解率 (accuracy score) を計算することで、ランダムフォレスト分類器 (Random Forest Classifier) を評価しましょう。

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```

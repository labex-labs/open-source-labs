# 性能の評価

最後に、テストセットに対する予測の正解率（accuracy）を計算することで、分類器の性能を評価します。

```python
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

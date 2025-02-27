# モデルを予測して評価する

学習済みのモデルを使用して、テスト用サブセット内のサンプルに対する数字の値を予測します。その後、`sklearn.metrics` の `metrics.classification_report()` および `metrics.ConfusionMatrixDisplay.from_predictions()` メソッドを使用してモデルを評価します。

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
```

# モデルの性能評価

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

テストデータを使用してターゲット値を予測し、`classification_report()`関数を使用してモデルの性能を評価します。また、`ConfusionMatrixDisplay()`関数を使用して混同行列を描画します。

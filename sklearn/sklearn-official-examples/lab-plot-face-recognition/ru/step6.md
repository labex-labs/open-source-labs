# Оценка производительности модели

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

Мы предсказываем целевые значения с использованием тестовых данных и оцениваем производительность модели с помощью функции `classification_report()`. Мы также строим матрицу ошибок (confusion matrix) с использованием функции `ConfusionMatrixDisplay()`.

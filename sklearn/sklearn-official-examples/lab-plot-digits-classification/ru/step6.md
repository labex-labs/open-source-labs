# Предсказание и оценка модели

Мы будем использовать обученную модель для предсказания значений цифр для образцов в тестовой подмножестве. Затем мы оценим модель с использованием методов `metrics.classification_report()` и `metrics.ConfusionMatrixDisplay.from_predictions()` из `sklearn.metrics`.

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

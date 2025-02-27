# Генерация матрицы ошибок

Мы сгенерируем матрицу ошибок с использованием класса ConfusionMatrixDisplay из scikit-learn. Матрица ошибок покажет количество правильных и неправильных предсказаний для каждого класса.

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```

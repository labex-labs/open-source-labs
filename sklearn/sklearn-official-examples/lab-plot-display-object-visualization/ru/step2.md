# Создание ConfusionMatrixDisplay

С использованием обученной модели мы вычисляем предсказания модели на тестовой выборке. Эти предсказания используются для вычисления матрицы ошибок, которая отображается с использованием `ConfusionMatrixDisplay`.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```

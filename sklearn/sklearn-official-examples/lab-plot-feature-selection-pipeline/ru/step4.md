# Оценка конвейера

Теперь оценим конвейер на тестовой подмножестве с использованием метода `predict`. Конвейер выберет 3 наиболее информативных признака на основе значения F-статистики ANOVA, а функция `LinearSVC` будет предсказывать значения на выбранных признаках.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```

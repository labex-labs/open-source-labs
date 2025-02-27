# Вычисление значений валидации

Мы будем использовать функцию `validation_curve` из scikit-learn для вычисления значений точности обучения и валидации для классификатора SVM с разными значениями gamma.

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```

# Вычисление оптимального числа итераций для тестовых данных

Мы также можем вычислить оптимальное число итераций для тестовых данных. Мы вычислим отрицательный логарифмический лосс для каждого числа итераций на тестовых данных.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```

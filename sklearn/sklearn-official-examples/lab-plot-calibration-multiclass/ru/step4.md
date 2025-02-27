# Сравнение log-loss

Мы сравниваем log-loss нескалиброванного и скалиброванного классификаторов на предсказаниях 1000 тестовых образцов.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-loss of")
print(f" * uncalibrated classifier: {score:.3f}")
print(f" * calibrated classifier: {cal_score:.3f}")
```

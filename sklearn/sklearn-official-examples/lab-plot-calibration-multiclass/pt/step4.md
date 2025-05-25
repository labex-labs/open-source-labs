# Comparação de Log-loss

Comparamos a perda de log do classificador não calibrado e calibrado nas previsões das 1000 amostras de teste.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Log-loss de")
print(f" * classificador não calibrado: {score:.3f}")
print(f" * classificador calibrado: {cal_score:.3f}")
```

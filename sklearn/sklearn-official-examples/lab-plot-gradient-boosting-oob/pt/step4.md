# Calcular o Melhor Número de Iterações para Dados de Teste

Também podemos calcular o melhor número de iterações para os dados de teste. Calcularemos a perda de log negativo para cada número de iterações nos dados de teste.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```

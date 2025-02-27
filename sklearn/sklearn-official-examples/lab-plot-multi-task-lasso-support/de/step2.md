# Modelle anpassen

Jetzt, wo wir unsere Daten haben, können wir Modelle an diese anpassen, indem wir die Lasso- und den Multi-Task-Lasso-Algorithmus verwenden. Wir werden ein Lasso-Modell für jede Aufgabe anpassen und anschließend ein Multi-Task-Lasso-Modell auf alle Aufgaben gleichzeitig anpassen.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

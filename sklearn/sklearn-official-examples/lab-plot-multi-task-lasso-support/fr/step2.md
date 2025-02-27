# Ajuster des modèles

Maintenant que nous avons nos données, nous pouvons ajuster des modèles à l'aide des algorithmes Lasso et Lasso multi-tâches. Nous ajusterons un modèle Lasso pour chaque tâche puis un modèle Lasso multi-tâches à toutes les tâches d'un coup.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

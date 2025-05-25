# Ajustar Modelos

Agora que temos nossos dados, podemos ajustar modelos a eles usando os algoritmos Lasso e Lasso multitarefa. Ajustaremos um modelo Lasso para cada tarefa e, em seguida, ajustaremos um modelo Lasso multitarefa a todas as tarefas de uma vez.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

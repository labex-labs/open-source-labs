# Ajustar modelos

Ahora que tenemos nuestros datos, podemos ajustar modelos a ellos utilizando los algoritmos Lasso y Lasso multitarea. Ajustaremos un modelo Lasso para cada tarea y luego ajustaremos un modelo Lasso multitarea a todas las tareas a la vez.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

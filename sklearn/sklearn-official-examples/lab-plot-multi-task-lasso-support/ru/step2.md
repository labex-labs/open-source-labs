# Подгонка моделей

Теперь, когда у нас есть наши данные, мы можем подгонять модели к ним с использованием алгоритмов Lasso и Lasso для многозадачности. Мы подгоним модель Lasso для каждой задачи, а затем сразу подгоним модель Lasso для многозадачности ко всем задачам.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

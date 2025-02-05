# Fit Models

Now that we have our data, we can fit models to it using the Lasso and multi-task Lasso algorithms. We will fit a Lasso model for each task and then fit a multi-task Lasso model to all tasks at once.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

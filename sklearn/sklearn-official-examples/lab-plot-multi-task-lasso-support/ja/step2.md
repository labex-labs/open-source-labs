# モデルの適合

データが用意できたので、Lasso とマルチタスク Lasso アルゴリズムを使ってモデルを適合させることができます。各タスクに対して Lasso モデルを適合させ、その後、すべてのタスクに対して一度にマルチタスク Lasso モデルを適合させます。

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

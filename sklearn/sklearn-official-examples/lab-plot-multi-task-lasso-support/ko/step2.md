# 모델 적합

이제 데이터가 준비되었으므로 Lasso 및 다중 작업 Lasso 알고리즘을 사용하여 모델을 적합시킬 수 있습니다. 각 작업에 대해 Lasso 모델을 적합시킨 다음 모든 작업에 대해 한 번에 다중 작업 Lasso 모델을 적합시킬 것입니다.

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```

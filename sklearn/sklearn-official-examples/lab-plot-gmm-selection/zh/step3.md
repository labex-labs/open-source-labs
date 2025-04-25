# 模型训练与选择

我们将组件数量从 1 变化到 6，并改变要使用的协方差参数类型：

- “full”：每个组件都有自己的通用协方差矩阵。
- “tied”：所有组件共享相同的通用协方差矩阵。
- “diag”：每个组件都有自己的对角协方差矩阵。
- “spherical”：每个组件都有自己的单一方差。

我们对不同的模型进行评分，并保留最佳模型（最低的 BIC）。这是通过使用`GridSearchCV`和一个用户定义的评分函数来完成的，该函数返回负的 BIC 分数。最佳参数集和估计器分别存储在`best_parameters_`和`best_estimator_`中。

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Callable to pass to GridSearchCV that will use the BIC score."""
    # Make it negative since GridSearchCV expects a score to maximize
    return -estimator.bic(X)

param_grid = {
    "n_components": range(1, 7),
    "covariance_type": ["spherical", "tied", "diag", "full"],
}
grid_search = GridSearchCV(
    GaussianMixture(), param_grid=param_grid, scoring=gmm_bic_score
)
grid_search.fit(X)
```

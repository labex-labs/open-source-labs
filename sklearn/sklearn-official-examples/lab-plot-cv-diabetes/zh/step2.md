# 应用 GridSearchCV

接下来，我们将应用 GridSearchCV 来找到套索回归的最佳 alpha 值。我们将使用从 10^-4 到 10^-0.5 的一系列 alpha 值，中间有 30 个值。我们将使用 5 折交叉验证。

```python
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=0, max_iter=10000)
alphas = np.logspace(-4, -0.5, 30)

tuned_parameters = [{"alpha": alphas}]
n_folds = 5

clf = GridSearchCV(lasso, tuned_parameters, cv=n_folds, refit=False)
clf.fit(X, y)
```

# 应用GridSearchCV

接下来，我们将应用GridSearchCV来找到套索回归的最佳alpha值。我们将使用从10^-4到10^-0.5的一系列alpha值，中间有30个值。我们将使用5折交叉验证。

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

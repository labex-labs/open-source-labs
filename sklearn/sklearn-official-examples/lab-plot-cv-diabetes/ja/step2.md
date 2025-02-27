# GridSearchCVを適用する

次に、GridSearchCVを適用してLasso回帰の最適なalpha値を見つけます。10^-4から10^-0.5までのalpha値の範囲を使い、その間に30個の値を設定します。交差検証には5分割を使用します。

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

# GridSearchCV 적용

다음으로, Lasso 회귀에 대한 최적의 alpha 값을 찾기 위해 GridSearchCV 를 적용합니다. 10^-4 에서 10^-0.5 까지의 alpha 값 범위를 사용하고 그 사이에 30 개의 값을 포함합니다. 교차 검증에는 5 개의 폴드를 사용합니다.

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

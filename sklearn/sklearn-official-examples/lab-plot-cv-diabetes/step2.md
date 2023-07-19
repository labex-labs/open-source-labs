# Apply GridSearchCV

Next, we will apply GridSearchCV to find the best alpha value for Lasso regression. We will use a range of alpha values from 10^-4 to 10^-0.5 with 30 values in between. We will use 5 folds for cross-validation.

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

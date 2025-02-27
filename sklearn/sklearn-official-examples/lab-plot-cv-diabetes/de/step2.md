# Anwenden von GridSearchCV

Als nächstes werden wir GridSearchCV anwenden, um den besten Alpha-Wert für die Lasso-Regression zu finden. Wir werden einen Bereich von Alpha-Werten von 10^-4 bis 10^-0,5 mit 30 Werten dazwischen verwenden. Wir werden 5 Folds für die Kreuzvalidierung verwenden.

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

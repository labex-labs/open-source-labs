# Aplicar GridSearchCV

A continuación, aplicaremos GridSearchCV para encontrar el mejor valor de alfa para la regresión Lasso. Usaremos una gama de valores de alfa desde 10^-4 hasta 10^-0.5 con 30 valores intermedios. Usaremos 5 pliegues para la validación cruzada.

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

# Aplicar GridSearchCV

Em seguida, aplicaremos GridSearchCV para encontrar o melhor valor de alfa para a regressão Lasso. Usaremos uma gama de valores de alfa de 10<sup>-4</sup> a 10<sup>-0.5</sup> com 30 valores intermédios. Usaremos 5 dobras para a validação cruzada.

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

# Appliquer GridSearchCV

Ensuite, nous allons appliquer GridSearchCV pour trouver la meilleure valeur d'alpha pour la régression Lasso. Nous utiliserons une plage de valeurs d'alpha allant de 10^-4 à 10^-0,5 avec 30 valeurs intermédiaires. Nous utiliserons 5 plis pour la validation croisée.

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

# Estimateurs validés croisés

Certains estimateurs dans scikit-learn ont des capacités de validation croisée intégrées. Ces estimateurs validés croisés sélectionnent automatiquement leurs paramètres par validation croisée, rendant le processus de sélection de modèle plus efficace.

```python
from sklearn import linear_model, datasets

# Créez un objet LassoCV
lasso = linear_model.LassoCV()

# Chargez l'ensemble de données du diabète
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Ajustez l'objet LassoCV sur l'ensemble de données
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```

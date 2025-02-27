# Entraîner le modèle

Maintenant, nous créons un objet de régression linéaire et entraînons le modèle à l'aide des ensembles d'entraînement.

```python
from sklearn import linear_model

# Créer un objet de régression linéaire
regr = linear_model.LinearRegression()

# Entraîner le modèle à l'aide des ensembles d'entraînement
regr.fit(diabetes_X_train, diabetes_y_train)
```

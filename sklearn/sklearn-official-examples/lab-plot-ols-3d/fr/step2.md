# Ajuster un modèle de régression linéaire

Ensuite, nous ajustons un modèle de régression linéaire à l'ensemble d'entraînement.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```

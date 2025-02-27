# Entraîner le modèle

Ensuite, nous allons entraîner un modèle de régression sur les données d'entraînement. Dans cet exemple, nous utiliserons un modèle de régression Ridge.

```python
from sklearn.linear_model import Ridge

# Entraîner le modèle de régression Ridge
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```

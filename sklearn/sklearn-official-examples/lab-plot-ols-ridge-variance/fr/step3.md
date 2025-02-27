# Définition des classifieurs

Dans cette étape, nous allons définir les classifieurs pour la régression linéaire ordinaire (OLS) et la régression Ridge.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```

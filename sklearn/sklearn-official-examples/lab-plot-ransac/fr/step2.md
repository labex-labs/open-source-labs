# Ajuster un modèle linéaire

Nous allons ajuster un modèle linéaire aux données à l'aide de la classe LinearRegression de scikit-learn.

```python
# Ajuster la droite en utilisant toutes les données
lr = linear_model.LinearRegression()
lr.fit(X, y)
```

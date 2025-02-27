# Étiqueter les points les plus incertains

Nous allons ajouter les étiquettes humaines aux points de données étiquetés et entraîner le modèle avec elles.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```

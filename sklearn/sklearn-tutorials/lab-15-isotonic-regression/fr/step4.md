# Prédire à l'aide du modèle

Après avoir ajusté le modèle, nous pouvons l'utiliser pour effectuer des prédictions sur de nouvelles données. Créons un nouveau tableau `X_new` et prédisons les valeurs cibles correspondantes.

```python
# Crée de nouvelles données pour la prédiction
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```

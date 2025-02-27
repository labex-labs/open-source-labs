# Prédire les données des modèles estimés

Nous allons prédire les données du modèle linéaire et du régresseur RANSAC et comparer leurs résultats.

```python
# Prédire les données des modèles estimés
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```

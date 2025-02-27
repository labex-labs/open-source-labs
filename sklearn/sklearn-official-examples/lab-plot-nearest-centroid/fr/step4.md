# Créez et ajustez le classifieur

Nous créons une instance du classifieur Nearest Centroid avec une valeur de réduction de 0,2 et ajustons les données.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```

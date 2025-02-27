# Rééchelle et faites tourner les données

Nous allons ensuite rééchelle et faire tourner les données pour la visualisation à l'aide de l'Analyse en Composantes Principales (PCA) de scikit-learn.

```python
# Rescale the data
pos *= np.sqrt((X_true**2).sum()) / np.sqrt((pos**2).sum())
npos *= np.sqrt((X_true**2).sum()) / np.sqrt((npos**2).sum())

# Rotate the data
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)
npos = clf.fit_transform(npos)
```

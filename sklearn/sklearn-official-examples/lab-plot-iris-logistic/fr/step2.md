# Créer une instance du classifieur de régression logistique et ajuster les données

Nous allons créer une instance du classifieur de régression logistique et ajuster les données.

```python
# Créer une instance du classifieur de régression logistique et ajuster les données.
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```

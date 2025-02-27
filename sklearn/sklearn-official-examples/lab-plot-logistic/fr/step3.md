# Ajustez le classifieur

Après avoir généré le jeu de données, nous allons ajuster le classifieur à l'aide de `LogisticRegression` de scikit-learn.

```python
# Ajustez le classifieur
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```

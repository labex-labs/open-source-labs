# Créez et entraînez le classifieur d'arbres de décision

Maintenant, nous pouvons créer et entraîner le classifieur d'arbres de décision à l'aide des données d'entraînement.

```python
# Créez un classifieur d'arbres de décision
clf = tree.DecisionTreeClassifier()

# Entraînez le classifieur
clf.fit(X_train, y_train)
```

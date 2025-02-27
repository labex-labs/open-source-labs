# Régression logistique

La régression logistique est une méthode de classification qui estime les probabilités des résultats possibles en utilisant une fonction logistique. Elle est couramment utilisée pour les tâches de classification binaire. La régression logistique peut également être étendue pour gérer les problèmes de classification multi-classe.

Ajustons un modèle de régression logistique.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- Nous créons une instance de `LogisticRegression` avec le paramètre `random_state` défini sur 0.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle de régression logistique.

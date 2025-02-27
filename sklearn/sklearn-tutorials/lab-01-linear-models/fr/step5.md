# Gradient stochastique (SGD)

Le Gradient stochastique (SGD) est une approche simple mais efficace pour entraîner des modèles linéaires. Il est particulièrement utile lorsque le nombre d'échantillons et de caractéristiques est très grand. Le SGD met à jour les paramètres du modèle en utilisant un sous-ensemble réduit des données d'entraînement à chaque itération, ce qui le rend adapté à l'apprentissage en ligne et à l'apprentissage hors mémoire.

Ajustons un modèle de régression logistique en utilisant le SGD.

```python
clf = linear_model.SGDClassifier(loss="log_loss", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- Nous créons une instance de `SGDClassifier` avec le paramètre `loss` défini sur "log_loss" pour effectuer une régression logistique.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle de régression logistique obtenu en utilisant le SGD.

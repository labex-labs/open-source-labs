# Perceptron

Le Perceptron est un algorithme de classification linéaire simple adapté à l'apprentissage à grande échelle. Il met à jour son modèle uniquement sur les erreurs, ce qui le rend plus rapide à entraîner que le gradient stochastique (SGD) avec une perte hinge. Les modèles résultants sont également plus creux.

Ajustons un modèle de perceptron.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

- Nous créons une instance de `Perceptron` avec le paramètre de régularisation `alpha` défini sur 0,1.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle de perceptron.

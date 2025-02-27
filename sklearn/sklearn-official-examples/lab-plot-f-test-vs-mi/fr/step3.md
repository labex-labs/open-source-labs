# Calcul du test F

Nous allons maintenant calculer le score du test F pour chaque caractéristique. Le test F ne capture que la dépendance linéaire entre les variables. Nous allons normaliser les scores du test F en les divisant par le score maximal du test F.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```

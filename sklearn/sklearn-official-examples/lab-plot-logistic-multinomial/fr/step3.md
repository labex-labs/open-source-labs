# Entraîner le modèle de régression logistique multinomiale

Nous allons maintenant entraîner un modèle de régression logistique multinomiale en utilisant la fonction `LogisticRegression` de scikit-learn. Nous définirons le solveur sur `"sag"`, le nombre maximum d'itérations sur 100, l'état aléatoire sur 42 et l'option multi-classe sur `"multinomial"`. Nous afficherons ensuite le score d'entraînement du modèle.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("score d'entraînement : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```

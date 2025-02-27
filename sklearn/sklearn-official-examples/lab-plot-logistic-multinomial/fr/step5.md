# Entraîner le modèle de régression logistique One-vs-Rest

Nous allons maintenant entraîner un modèle de régression logistique One-vs-Rest en utilisant les mêmes paramètres que dans l'Étape 3, mais avec l'option multi-classe définie sur `"ovr"`. Nous afficherons ensuite le score d'entraînement du modèle.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("score d'entraînement : %.3f (%s)" % (clf.score(X, y), "ovr"))
```

# Entraîner et tester les classifieurs

Nous allons entraîner et tester chaque classifieur pour voir comment ils se comportent sur les données générées. Nous allons répéter ce processus plusieurs fois pour obtenir une note de précision moyenne.

```python
n_train = 20  # échantillons pour l'entraînement
n_test = 200  # échantillons pour le test
n_averages = 50  # combien de fois répéter la classification
n_features_max = 75  # nombre maximum de caractéristiques
step = 4  # pas de calcul

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```

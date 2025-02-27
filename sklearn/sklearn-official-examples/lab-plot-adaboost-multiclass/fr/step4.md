# Créer et entraîner les modèles

Nous allons créer deux modèles AdaBoost, l'un utilisant SAMME et l'autre utilisant SAMME.R. Les deux modèles utiliseront DecisionTreeClassifier avec une profondeur maximale de 2 et 300 estimateurs.

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```

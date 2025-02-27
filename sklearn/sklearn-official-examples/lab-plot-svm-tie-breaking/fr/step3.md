# Création d'un modèle SVM avec et sans tri en cas d'égalité

Dans cette étape, nous allons créer deux modèles SVM - l'un avec le tri en cas d'égalité désactivé et l'autre avec le tri en cas d'égalité activé. Nous allons utiliser la classe `SVC` de scikit-learn pour créer ces modèles. Le paramètre `break_ties` est défini sur `False` et `True` pour les deux modèles, respectivement.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```

# Tracer la dépendance partielle pour deux fonctionnalités

Dans cette étape, nous allons tracer les courbes de dépendance partielle pour les fonctionnalités "âge" et "imc" (indice de masse corporelle) pour l'arbre de décision. Avec deux fonctionnalités, `PartialDependenceDisplay.from_estimator` s'attend à tracer deux courbes. Ici, la fonction de tracé place une grille de deux graphiques en utilisant l'espace défini par `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

Les courbes de dépendance partielle peuvent être tracées pour le perceptron multicouche. Dans ce cas, `line_kw` est passé à `PartialDependenceDisplay.from_estimator` pour changer la couleur de la courbe.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```

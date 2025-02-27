# Tracer la dépendance partielle pour une fonctionnalité

Dans cette étape, nous allons tracer les courbes de dépendance partielle pour une seule fonctionnalité, "âge", sur les mêmes axes. Dans ce cas, `tree_disp.axes_` est passé à la deuxième fonction de tracé.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```

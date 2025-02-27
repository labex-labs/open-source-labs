# Tracer la dépendance partielle des deux modèles ensemble

Dans cette étape, nous allons tracer les courbes de dépendance partielle des deux modèles sur le même graphique.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Une autre manière de comparer les courbes est de les superposer. Ici, nous créons une figure avec une ligne et deux colonnes. Les axes sont passés à la fonction `PartialDependenceDisplay.plot` sous forme de liste, qui dessinera les courbes de dépendance partielle de chaque modèle sur les mêmes axes. La longueur de la liste d'axes doit être égale au nombre de graphiques tracés.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` est un conteneur numpy des axes utilisés pour tracer les graphiques de dépendance partielle. Cela peut être passé à `mlp_disp` pour avoir le même effet de tracé des graphiques les uns sur les autres. De plus, `mlp_disp.figure_` stocke la figure, ce qui permet de redimensionner la figure après avoir appelé `plot`. Dans ce cas, `tree_disp.axes_` a deux dimensions, donc `plot` ne montrera que l'étiquette y et les graduations y sur le graphique le plus à gauche.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```

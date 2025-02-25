# Ajouter un effet de trait à du texte

Nous pouvons ajouter un effet de trait à du texte en utilisant l'effet de tracé `withStroke`. Dans cet exemple, nous allons ajouter un effet de trait au texte d'annotation dans le graphique.

```python
# Créer le graphique et ajouter l'annotation de texte avec effet de trait
fig, ax = plt.subplots()
ax.imshow(arr)
txt = ax.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[patheffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    patheffects.Stroke(linewidth=5, foreground="w"),
    patheffects.Normal()])

# Ajouter une grille avec effet de trait
pe = [patheffects.withStroke(linewidth=3,
                             foreground="w")]
ax.grid(True, linestyle="-", path_effects=pe)

plt.show()
```

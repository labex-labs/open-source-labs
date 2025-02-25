# Ajouter un effet de trait aux lignes de contour

Nous pouvons également ajouter des effets de trait aux lignes de contour et à leurs étiquettes en utilisant l'effet de tracé `withStroke`.

```python
# Créer le graphique et ajouter les lignes de contour avec effet de trait
fig, ax = plt.subplots()
ax.imshow(arr)
cntr = ax.contour(arr, colors="k")

plt.setp(cntr.collections, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

clbls = ax.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

plt.show()
```

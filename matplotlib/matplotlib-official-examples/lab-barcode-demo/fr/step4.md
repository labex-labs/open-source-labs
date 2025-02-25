# Créez la figure et les axes

Nous devons créer la figure et les axes pour le code-barres. Nous définirons la taille de la figure comme étant un multiple du nombre de points de données, et nous désactiverons tous les axes.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # couvre toute la figure
ax.set_axis_off()
```

# Configurez le rectangle

Nous allons définir la position et les dimensions du rectangle en utilisant les variables `left`, `bottom`, `width` et `height`. Ensuite, nous créerons le rectangle à l'aide de la classe `Rectangle` et l'ajouterons à la figure à l'aide de la méthode `add_patch`.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```

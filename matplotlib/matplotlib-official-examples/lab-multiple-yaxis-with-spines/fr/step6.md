# Réglez les limites et les étiquettes pour les axes

Nous réglons les limites et les étiquettes pour chaque axe y en utilisant la méthode `set`. Nous définissons également la couleur des étiquettes pour correspondre à la couleur des lignes en utilisant la méthode `set_color`.

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Densité")
twin1.set(ylim=(0, 4), ylabel="Température")
twin2.set(ylim=(1, 65), ylabel="Vitesse")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```

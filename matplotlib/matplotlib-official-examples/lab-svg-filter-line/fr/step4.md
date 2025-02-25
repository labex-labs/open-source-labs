# Dessiner des ombres

Nous dessinons des ombres pour les lignes en utilisant les mêmes lignes avec un léger décalage et des couleurs grises. Nous ajustons la couleur et le zorder des lignes d'ombre de sorte qu'elles soient dessinées en dessous des lignes d'origine. Nous utilisons également la méthode `offset_copy()` pour créer une transformation de décalage pour les lignes d'ombre.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```

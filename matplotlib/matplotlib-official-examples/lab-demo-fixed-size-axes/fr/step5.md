# Ajouter des axes à la figure

Nous allons ajouter les axes à la figure à l'aide de la fonction `add_axes()` en passant la position de l'objet `Divider`.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```

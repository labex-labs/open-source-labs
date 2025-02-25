# Laisser de la place pour l'étiquette de l'axe des y et ajuster les axes

Dans cette étape, nous utilisons la méthode `make_axes_area_auto_adjustable` pour laisser de la place pour l'étiquette de l'axe des y dans les deux axes. Nous utilisons également le paramètre `use_axes` pour spécifier les axes à ajuster et le paramètre `pad` pour ajuster l'espacement entre les axes.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```

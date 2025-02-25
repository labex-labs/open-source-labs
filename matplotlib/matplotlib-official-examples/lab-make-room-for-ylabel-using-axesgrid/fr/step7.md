# Ajuster les axes et laisser de la place pour l'étiquette de l'axe des y

Dans cette étape, nous utilisons la méthode `add_auto_adjustable_area` pour ajuster les axes et laisser de la place pour l'étiquette de l'axe des y. Nous définissons également le titre et l'étiquette de l'axe des x pour le second axe.

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["very long label"])
ax2.set_title("Title")
ax2.set_xlabel("X - Label")
```

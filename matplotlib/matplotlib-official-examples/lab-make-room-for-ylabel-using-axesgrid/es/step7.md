# Ajustar los ejes y hacer espacio para la etiqueta del eje y

En este paso, usamos el método `add_auto_adjustable_area` para ajustar los ejes y hacer espacio para la etiqueta del eje y. También establecemos el título y la etiqueta del eje x para el segundo eje.

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

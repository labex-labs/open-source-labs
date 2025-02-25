# Étiquetage en dehors des axes

Nous pouvons préférer les étiquettes en dehors des axes tout en les alignant les unes avec les autres. Dans ce cas, nous utilisons une transformation légèrement différente.

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```

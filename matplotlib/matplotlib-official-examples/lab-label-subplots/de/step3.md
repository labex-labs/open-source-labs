# Bezeichnung innerhalb der Achsen

Die einfachste Methode, um Teilbilder zu beschriften, besteht darin, die Bezeichnung innerhalb der Achsen zu platzieren. Wir können dies mit der `ax.text`-Methode erreichen. Wir werden durch jedes Teilbild iterieren und die Bezeichnung innerhalb der Achse mit `ax.transAxes` hinzufügen.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

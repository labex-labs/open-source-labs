# Bezeichnung außerhalb der Achsen

Wir möchten möglicherweise die Bezeichnungen außerhalb der Achsen, aber immer noch zueinander ausgerichtet haben. In diesem Fall verwenden wir eine leicht andere Transformation.

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```

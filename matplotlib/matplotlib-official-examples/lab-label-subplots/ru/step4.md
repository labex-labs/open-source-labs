# Метка вне осей

Может быть, мы предпочитаем метки вне осей, но при этом они должны быть выровнены друг с другом. В этом случае мы используем немного другой трансформ.

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```

# Label Inside the Axes

The simplest method to label subplots is to put the label inside the axes. We can achieve this by using the `ax.text` method. We will loop through each subplot and add the label inside the axes using `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

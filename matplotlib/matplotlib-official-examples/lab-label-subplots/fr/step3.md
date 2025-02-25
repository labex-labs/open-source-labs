# Étiquetage à l'intérieur des axes

La méthode la plus simple pour étiqueter les sous-graphiques consiste à placer l'étiquette à l'intérieur des axes. Nous pouvons le faire en utilisant la méthode `ax.text`. Nous allons parcourir chaque sous-graphique et ajouter l'étiquette à l'intérieur des axes en utilisant `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

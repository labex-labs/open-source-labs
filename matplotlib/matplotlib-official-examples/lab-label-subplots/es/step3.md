# Etiquetar dentro de los ejes

El método más simple para etiquetar subgráficos es poner la etiqueta dentro de los ejes. Esto se puede lograr utilizando el método `ax.text`. Recorreremos cada subgráfico y agregaremos la etiqueta dentro de los ejes utilizando `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

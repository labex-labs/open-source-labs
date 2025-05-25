# Rotular Dentro dos Eixos

O método mais simples para rotular subplots é colocar o rótulo dentro dos eixos. Podemos conseguir isso usando o método `ax.text`. Iremos iterar por cada subplot e adicionar o rótulo dentro dos eixos usando `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

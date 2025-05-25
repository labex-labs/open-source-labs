# Criar LineCollection usando deslocamentos (offsets)

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

O quarto passo é criar um LineCollection usando deslocamentos (offsets). Usaremos o LineCollection para criar curvas com deslocamentos. Também usaremos o offset_transform para definir as posições das curvas.

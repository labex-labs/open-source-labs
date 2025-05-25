# Criar PolyCollection usando deslocamentos (offsets)

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

O quinto passo é criar um PolyCollection usando deslocamentos (offsets). Usaremos o PolyCollection para preencher as curvas com cores. Também usaremos o offset_transform para definir as posições das curvas.

# Adicionar uma Barra de Cores (Colorbar)

Adicione uma barra de cores ao eixo inserido usando a função `inset_axes`. Defina a largura, altura, localização e bounding box da barra de cores.

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```

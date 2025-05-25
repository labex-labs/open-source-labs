# Criar um BboxImage para cada mapa de cores (colormap)

Em seguida, criamos um BboxImage para cada mapa de cores. Começamos criando uma lista de todos os mapas de cores usando o método `plt.colormaps`. Em seguida, criamos um loop `for` que itera através da lista de mapas de cores. Para cada mapa de cores, calculamos as posições `ix` e `iy` usando o método `divmod()`. Depois, criamos um objeto `Bbox` usando o método `Bbox.from_bounds()`. Passamos os valores `ix`, `iy`, `dx` e `dy` para o método `Bbox.from_bounds()` para criar a caixa delimitadora (bounding box). Em seguida, criamos um objeto `TransformedBbox` usando o objeto `Bbox` e o objeto `ax2.transAxes`. Finalmente, criamos um objeto `BboxImage` usando o método `add_artist()`. Passamos o objeto `TransformedBbox` para o construtor `BboxImage` para criar uma imagem com o mapa de cores.

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```

# Usar uma Norma de Limite (Boundary Norm)

Usaremos, em vez disso, uma norma de limite para colorir os segmentos de linha. Criaremos um `ListedColormap` contendo três cores - vermelho, verde e azul. Em seguida, criaremos um `BoundaryNorm` com limites -1, -0.5, 0.5 e 1, e o `ListedColormap`. Usaremos a função `set_array` para definir os valores usados para o colormapping.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```

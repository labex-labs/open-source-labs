# Criar os Polígonos e Adicionar ao Gráfico

Criamos os polígonos usando a função `PolyCollection` do Matplotlib e adicionamos-os ao gráfico.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```

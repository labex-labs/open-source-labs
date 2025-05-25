# Desenhar um Círculo na Parede

Desenhar-se-á um círculo na 'parede' x=0 do gráfico 3D usando as funções `Circle` e `pathpatch_2d_to_3d` do Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```

# Создаем полигоны и добавляем их на график

Мы создаем полигоны с использованием функции `PolyCollection` из Matplotlib и добавляем их на график.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```

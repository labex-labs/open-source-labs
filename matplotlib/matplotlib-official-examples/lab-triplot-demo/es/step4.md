# Trazar la triangulación de Delaunay

Vamos a trazar la triangulación utilizando la función triplot.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot of Delaunay Triangulation')
```

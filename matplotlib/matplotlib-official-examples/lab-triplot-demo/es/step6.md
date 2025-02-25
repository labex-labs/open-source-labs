# Trazar la triangulación especificada por el usuario

Vamos a trazar la triangulación especificada por el usuario utilizando la función triplot.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
ax2.triplot(x, y, triangles, 'go-', lw=1.0)
ax2.set_title('Triplot of User-Specified Triangulation')
ax2.set_xlabel('Longitude (grados)')
ax2.set_ylabel('Latitud (grados)')
```

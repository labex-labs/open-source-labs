# Delaunay-Triangulation darstellen

Wir werden die Triangulation mit der triplot-Funktion darstellen.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot of Delaunay Triangulation')
```

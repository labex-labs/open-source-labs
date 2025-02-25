# Inverser la flèche d'orientation

Si vous voulez inverser la flèche d'orientation, vous pouvez changer le type de marqueur de `>` à `<`.

```python
# Pour inverser la flèche d'orientation, changez le type de marqueur de > à <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

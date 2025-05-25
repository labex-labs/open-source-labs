# Inverter a Seta de Orientação

Se você deseja inverter a seta de orientação, pode mudar o tipo de marcador de `>` para `<`.

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

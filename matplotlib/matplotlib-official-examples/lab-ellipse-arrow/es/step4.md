# Invertir la flecha de orientación

Si desea invertir la flecha de orientación, puede cambiar el tipo de marcador de `>` a `<`.

```python
# Para invertir la flecha de orientación, cambie el tipo de marcador de > a <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

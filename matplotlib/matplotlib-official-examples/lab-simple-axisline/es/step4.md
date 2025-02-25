# Hacer visible la línea del eje x en y = 0

Ahora haremos visible la línea del eje x en y = 0. Esto se hace estableciendo el eje xzero como visible.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```

# Agregar texto a la gráfica

Puede agregar texto a su gráfica utilizando la función `ax.text()`. En este ejemplo, agregaremos texto con diferentes familias de fuentes.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```

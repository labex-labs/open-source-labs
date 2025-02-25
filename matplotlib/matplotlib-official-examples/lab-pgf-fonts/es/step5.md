# Agregar texto a la gráfica

Agregaremos texto a la gráfica utilizando la función `ax.text()`. Agregaremos texto a cuatro ubicaciones diferentes en la gráfica, cada una con una familia de fuentes diferente: serif, monospace, sans-serif y cursiva.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```

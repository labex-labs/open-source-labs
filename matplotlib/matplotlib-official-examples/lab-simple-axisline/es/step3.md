# Ocultar los ejes superior y derecho

Ahora ocultaremos los ejes superior y derecho, ya que solo necesitamos los ejes izquierdo y inferior.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```

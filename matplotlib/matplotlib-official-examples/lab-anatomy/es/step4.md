# Agregar etiquetas y título

Ahora agregaremos etiquetas a los ejes x e y, y un título a la figura usando los métodos `set_xlabel()`, `set_ylabel()` y `set_title()`.

```python
# Agregar etiquetas y título
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```

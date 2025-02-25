# Configurar el estilo de los ejes

Ahora configuraremos el estilo de los ejes agregando flechas al final de cada eje y agregando los ejes X e Y desde el origen.

```python
for direction in ["xzero", "yzero"]:
    # agrega flechas al final de cada eje
    ax.axis[direction].set_axisline_style("-|>")
    # agrega los ejes X e Y desde el origen
    ax.axis[direction].set_visible(True)

# oculta los bordes
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```

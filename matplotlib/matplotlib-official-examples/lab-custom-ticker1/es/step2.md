# Definir la función de cotizador personalizado

A continuación, debemos definir la función de cotizador personalizado. La función de cotizador personalizado toma dos argumentos: el valor y la posición de la marca, y devuelve la etiqueta de la marca formateada. En este caso, formatearemos la etiqueta de la marca como dólares en millones.

```python
def millions(x, pos):
    """Los dos argumentos son el valor y la posición de la marca."""
    return f'${x*1e-6:1.1f}M'
```

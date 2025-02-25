# Especificar el tamaño de celda

Si necesita una exageración vertical topográficamente precisa, o no desea adivinar cuál debería ser el valor de `vert_exag`, tendrá que especificar el tamaño de celda de la cuadrícula (es decir, los parámetros `dx` y `dy`). De lo contrario, cualquier valor de `vert_exag` que especifique será relativo al espaciado de la cuadrícula de sus datos de entrada. En este paso, calculamos los valores de `dx` y `dy` en metros.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```

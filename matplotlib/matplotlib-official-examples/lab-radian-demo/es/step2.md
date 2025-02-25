# Crear datos

Crea una matriz de valores entre 0 y 15 en incrementos de 0,01, y conviértelos a radianes utilizando la función radians del paquete basic_units.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```

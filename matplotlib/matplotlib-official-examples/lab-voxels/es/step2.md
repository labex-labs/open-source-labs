# Preparar coordenadas

A continuación, prepararemos las coordenadas para nuestro gráfico de voxeles. Crearemos una cuadrícula de puntos de 8x8x8 utilizando la función `indices` de NumPy.

```python
x, y, z = np.indices((8, 8, 8))
```

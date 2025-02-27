# Definir la matriz de conectividad

En este paso, definiremos la matriz de conectividad utilizando la función `grid_to_graph` de scikit-learn. Esta función crea un gráfico de conectividad basado en la cuadrícula de píxeles de las imágenes.

```python
connectivity = grid_to_graph(*images[0].shape)
```

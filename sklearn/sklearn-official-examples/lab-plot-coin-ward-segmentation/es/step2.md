# Definir la estructura de los datos

Los píxeles en una imagen están conectados a sus vecinos. Para realizar el agrupamiento jerárquico en una imagen, necesitamos definir la estructura de los datos. Podemos usar la función `grid_to_graph` de scikit-learn para crear una matriz de conectividad que defina la estructura de los datos.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```

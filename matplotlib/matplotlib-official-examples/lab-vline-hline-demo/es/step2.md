# Definir datos

El siguiente paso es definir los datos que usaremos en nuestro gráfico. Usaremos la función `arange` de NumPy para crear una matriz de valores que van desde 0 hasta 5 con un paso de 0,1. Usaremos esta matriz como el eje x. También definiremos el eje y usando la función exponencial y la función seno de NumPy.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```

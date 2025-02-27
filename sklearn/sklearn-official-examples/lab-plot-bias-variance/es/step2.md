# Establecer los parámetros

Necesitamos establecer los parámetros que controlan el tamaño de los conjuntos de datos, el número de iteraciones y la desviación estándar del ruido.

```python
n_repeat = 50  # Número de iteraciones para calcular las expectativas
n_train = 50  # Tamaño del conjunto de entrenamiento
n_test = 1000  # Tamaño del conjunto de prueba
noise = 0.1  # Desviación estándar del ruido
np.random.seed(0)
```

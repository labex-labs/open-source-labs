# Crear un conjunto de datos con pesos

Creamos un conjunto de datos con pesos utilizando la biblioteca numpy. Generamos 20 puntos con valores aleatorios y asignamos un peso mayor a las últimas 10 muestras.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```

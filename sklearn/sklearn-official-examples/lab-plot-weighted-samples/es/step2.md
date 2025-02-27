# Crear datos

Crearemos un conjunto de datos de 20 puntos, donde los primeros 10 puntos pertenecen a la clase 1 y los últimos 10 puntos pertenecen a la clase -1.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```

# Generar datos

Generamos 40 puntos separables utilizando la función `random.randn` de numpy. Los primeros 20 puntos tienen una media de [-2, -2] y los siguientes 20 puntos tienen una media de [2, 2]. Luego asignamos una etiqueta de clase 0 a los primeros 20 puntos y una etiqueta de clase 1 a los siguientes 20 puntos.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```

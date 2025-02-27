# Generar el conjunto de datos

A continuación, generamos un conjunto de datos que contiene dos círculos concéntricos usando `make_circles`. Asignamos etiquetas al conjunto de datos de modo que todas las muestras son desconocidas excepto dos muestras que pertenecen respectivamente al círculo exterior y al círculo interior.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```

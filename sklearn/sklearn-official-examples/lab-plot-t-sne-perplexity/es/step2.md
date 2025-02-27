# Crear datos

Vamos a crear tres conjuntos de datos diferentes para ilustrar el uso de t-SNE. El primer conjunto de datos será dos círculos concéntricos.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```

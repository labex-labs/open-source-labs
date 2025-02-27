# Cargar o generar conjuntos de datos pequeños

Ahora, necesitamos cargar o generar los conjuntos de datos pequeños que usaremos para este ejemplo. Usaremos el conjunto de datos iris, el conjunto de datos digits y dos conjuntos de datos generados usando las funciones make_circles y make_moons.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```

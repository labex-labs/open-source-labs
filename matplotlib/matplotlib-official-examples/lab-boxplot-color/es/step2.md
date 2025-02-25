# Creando datos de prueba aleatorios

A continuación, crearemos datos de prueba aleatorios utilizando la biblioteca `numpy`. Generaremos 3 conjuntos de datos, cada uno con una desviación estándar diferente.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```

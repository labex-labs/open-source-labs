# Crear un conjunto de datos de muestra

Crearemos un conjunto de datos de muestra utilizando la biblioteca numpy. Crearemos seis conjuntos de datos con diferentes desviaciones estándar.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```

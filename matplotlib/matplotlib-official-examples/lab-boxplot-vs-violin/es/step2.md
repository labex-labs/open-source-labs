# Generar datos

Generaremos algunos datos de prueba aleatorios utilizando numpy.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```

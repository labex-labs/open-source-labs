# Generar algunos datos de muestra

A continuación, generaremos algunos datos de muestra para realizar la estimación de densidad. Con el fin de este laboratorio, generemos un conjunto de datos unidimensional con 100 puntos. Usaremos una distribución normal para generar los datos.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```

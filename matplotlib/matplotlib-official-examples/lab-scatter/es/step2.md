# Generar datos aleatorios

En este paso, generaremos datos aleatorios para nuestro diagrama de dispersión. Generaremos 50 puntos de datos para cada variable utilizando la biblioteca NumPy.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```

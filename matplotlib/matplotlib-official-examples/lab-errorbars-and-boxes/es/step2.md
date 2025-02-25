# Preparar los datos

Luego, prepararemos los datos para nuestro diagrama de caja. Crearemos algunos datos ficticios para los valores de x e y, así como para los valores de error.

```python
# Número de puntos de datos
n = 5

# Datos ficticios
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Errores ficticios (por encima y por debajo)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```

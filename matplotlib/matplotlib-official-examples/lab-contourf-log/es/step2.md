# Generar el conjunto de datos

Generaremos un conjunto de datos con valores positivos y negativos usando `numpy`:

```python
N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)

X, Y = np.meshgrid(x, y)

# Una pequeña protuberancia con una punta saliendo.
# Necesita tener el eje z/color en una escala logarítmica, para que veamos tanto la protuberancia como la punta.
# Una escala lineal solo muestra la punta.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
z = Z1 + 50 * Z2

# Ponga algunos valores negativos (esquina inferior izquierda) para causar problemas con los logs:
z[:5, :5] = -1

# Lo siguiente no es estrictamente esencial, pero eliminará
# una advertencia.  Coméntelo para ver la advertencia.
z = ma.masked_where(z <= 0, z)
```

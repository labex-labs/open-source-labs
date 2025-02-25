# Crear datos

A continuación, creamos los datos que utilizaremos en nuestra gráfica. En este ejemplo, usaremos NumPy para generar los datos.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```

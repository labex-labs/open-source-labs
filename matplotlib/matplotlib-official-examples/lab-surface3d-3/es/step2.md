# Crear datos para la representación gráfica de superficie

En este paso, crearemos los datos para la representación gráfica de superficie. Crearemos una malla de valores de X e Y, calcularemos la distancia radial R y calcularemos el valor de Z basado en el valor de R usando `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

# Generar datos

A continuación, generaremos los datos que usaremos para crear el gráfico de contorno. En esta práctica, usaremos la función `np.meshgrid()` para crear las coordenadas X, Y y Z.

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

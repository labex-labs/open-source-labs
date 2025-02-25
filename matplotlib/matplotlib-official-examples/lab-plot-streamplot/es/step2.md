# Crear datos

Vamos a crear los datos para nuestro gráfico de flujo usando la biblioteca Numpy. En este ejemplo, crearemos una malla (meshgrid) con 100 puntos en ambas direcciones y calcularemos los componentes U y V de nuestro campo vectorial.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```

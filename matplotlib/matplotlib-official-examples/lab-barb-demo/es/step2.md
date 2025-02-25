# Crear datos

A continuación, crearemos los datos que se utilizarán para generar el gráfico de barbas de viento. Crearemos una cuadrícula uniforme de 5x5 y un campo vectorial utilizando las funciones meshgrid y multiplicación.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```

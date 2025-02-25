# Crear la cuadrícula

A continuación, crearemos una cuadrícula de puntos en la que mostraremos el campo de vectores. En este ejemplo, crearemos una malla de puntos utilizando la función `meshgrid` de NumPy. La función `arange` se utiliza para crear una matriz de puntos equidistantes dentro de un intervalo especificado.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```

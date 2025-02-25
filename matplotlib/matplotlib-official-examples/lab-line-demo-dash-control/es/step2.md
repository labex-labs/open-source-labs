# Crear datos para graficar

A continuación, necesitamos crear algunos datos para graficar. En este laboratorio, usaremos la función seno para crear nuestros datos. Generaremos 500 puntos equidistantes entre 0 y 10 y calcularemos el seno de cada punto usando la función `np.sin()`.

```python
x = np.linspace(0, 10, 500)
y = np.sin(x)
```

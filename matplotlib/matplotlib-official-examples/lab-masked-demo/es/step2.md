# Crear datos para graficar

Vamos a crear datos para graficar usando NumPy. Generaremos 31 puntos de datos entre -pi/2 y pi/2 y calcularemos el coseno de estos valores elevados a la tercera potencia.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```

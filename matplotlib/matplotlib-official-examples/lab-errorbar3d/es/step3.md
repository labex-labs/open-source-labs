# Generar datos para el gráfico

Generamos los datos para nuestro gráfico creando una curva paramétrica. Una curva paramétrica es un conjunto de ecuaciones que describen las coordenadas x, y y z en función de un parámetro. Utilizamos la función `arange` de NumPy para crear una matriz de valores de 0 a 2π. Luego utilizamos estos valores para calcular las coordenadas x, y y z utilizando funciones trigonométricas.

```python
t = np.arange(0, 2*np.pi+.1, 0.01)
x, y, z = np.sin(t), np.cos(3*t), np.sin(5*t)
```

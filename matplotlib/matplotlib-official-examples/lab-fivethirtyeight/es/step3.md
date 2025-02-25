# Crear datos para el gráfico de líneas

En este paso, crearemos los datos para nuestro gráfico de líneas. Usaremos la función `linspace` de NumPy para crear una matriz de valores espaciados uniformemente entre 0 y 10. También generaremos algo de ruido aleatorio usando la función `random.randn` de NumPy.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```

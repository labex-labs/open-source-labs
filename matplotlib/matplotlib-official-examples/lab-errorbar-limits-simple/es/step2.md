# Crear los datos

En este paso, creamos los datos que usaremos para crear nuestra gráfica de barras de error.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```

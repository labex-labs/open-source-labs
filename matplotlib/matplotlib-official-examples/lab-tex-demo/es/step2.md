# Crear un diagrama de líneas simple

En este paso, crearemos un diagrama de líneas simple utilizando Matplotlib. Comenzaremos generando algunos datos para graficar utilizando la función `linspace()` de NumPy y la función `cos()`. Luego, utilizaremos la función `plot()` para crear el gráfico.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```

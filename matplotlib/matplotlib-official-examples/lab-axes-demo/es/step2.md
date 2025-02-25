# Generar datos

En este paso, generamos algunos datos para utilizar en el gráfico. Crearemos un ruido coloreado gaussiano utilizando la función `convolve` de NumPy y lo graficaremos utilizando Matplotlib.

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```

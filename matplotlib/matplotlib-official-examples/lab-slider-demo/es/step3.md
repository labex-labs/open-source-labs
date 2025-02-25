# Crear la gráfica inicial

Ahora, crearemos la gráfica inicial de la onda sinusoidal. Definiremos los parámetros iniciales para la amplitud y la frecuencia y graficaremos la onda sinusoidal utilizando esos parámetros.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```

# Configurar la trama inicial

A continuación, configuraremos la trama inicial. Crearemos una onda senoidal con una frecuencia de 2 Hz utilizando la función `arange` de `numpy`, y la representaremos utilizando la función `plot` de `matplotlib.pyplot`.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```

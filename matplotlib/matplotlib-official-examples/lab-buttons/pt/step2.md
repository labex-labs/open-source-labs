# Configurar o gráfico inicial

Em seguida, configuraremos o gráfico inicial. Criaremos uma onda senoidal com uma frequência de 2 Hz usando a função `arange` do `numpy` e a plotaremos usando a função `plot` do `matplotlib.pyplot`.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```

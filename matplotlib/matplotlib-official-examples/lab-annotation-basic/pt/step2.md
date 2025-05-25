# Criar um Gráfico

Em seguida, criaremos um gráfico usando Matplotlib. Neste exemplo, plotaremos a função cosseno em um intervalo de valores.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```

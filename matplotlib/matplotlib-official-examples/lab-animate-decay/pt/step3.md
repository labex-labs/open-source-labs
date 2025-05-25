# Configurar o gráfico

Agora, precisamos configurar o gráfico. Criaremos uma figura e um objeto de eixos usando a função `subplots()` do Matplotlib. Também criaremos um objeto de linha para representar a onda senoidal.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```

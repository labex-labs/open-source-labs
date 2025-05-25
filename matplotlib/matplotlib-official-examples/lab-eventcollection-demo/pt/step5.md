# Criar o gráfico

Criaremos o gráfico usando a função `matplotlib.pyplot.plot()`.

```python
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')
```

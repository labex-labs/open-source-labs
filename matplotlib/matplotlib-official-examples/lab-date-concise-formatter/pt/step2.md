# Formatador de Data Conciso

Em seguida, exploramos o `~.dates.ConciseDateFormatter` e sua saída. Criamos um novo gráfico com o formatador de data conciso e vemos como ele difere do formatador padrão.

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```

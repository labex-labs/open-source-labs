# Criando um Gráfico Stem

Em seguida, criaremos um gráfico stem com alguma variação nos níveis para distinguir eventos próximos. Adicionamos marcadores na linha de base para ênfase visual na natureza unidimensional da linha do tempo. Para cada evento, adicionamos um rótulo de texto via `~.Axes.annotate`, que é deslocado em unidades de pontos a partir da ponta da linha do evento. Aqui está o código para criar um gráfico stem:

```python
# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```

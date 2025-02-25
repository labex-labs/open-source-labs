# Formateur de date concise

Ensuite, nous explorons le `~.dates.ConciseDateFormatter` et sa sortie. Nous créons un nouveau tracé avec le formateur de date concise et observons comment il diffère du formateur par défaut.

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Formateur de date concise')
plt.show()
```

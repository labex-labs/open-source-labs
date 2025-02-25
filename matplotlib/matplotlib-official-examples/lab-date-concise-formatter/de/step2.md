# Kürzerer Datumsformatter

Als nächstes untersuchen wir den `~.dates.ConciseDateFormatter` und seine Ausgabe. Wir erstellen ein neues Diagramm mit dem kürzeren Datumsformatter und sehen, wie es sich von dem Standardformatter unterscheidet.

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

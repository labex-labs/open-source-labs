# Fügen Sie globalen x- und y-Beschriftungen zu einer Grafik hinzu

Als nächstes werden wir globalen x- und y-Beschriftungen zu einer Grafik hinzufügen, die die relativen Aktienkurse verschiedener Unternehmen im Laufe der Zeit zeigt. Wir werden die `np.genfromtxt()`-Funktion verwenden, um eine CSV-Datei mit Aktienkursdaten einzulesen und dann die Daten für jedes Unternehmen mit Hilfe von Teilgrafiken darzustellen. Wir werden die `fig.supxlabel()`- und `fig.supylabel()`-Methoden verwenden, um globale x- und y-Beschriftungen zur Grafik hinzuzufügen.

```python
from matplotlib.cbook import get_sample_data

with get_sample_data('Stocks.csv') as file:
    stocks = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex=True, sharey=True)
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = stocks[column_name]
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Jahr')
fig.supylabel('Aktienkurs relativ zum Maximum')

plt.show()
```

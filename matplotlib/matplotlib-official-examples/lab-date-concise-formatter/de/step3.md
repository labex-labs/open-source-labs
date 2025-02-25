# Registrieren eines Konverters

Wenn alle Aufrufe von Achsen, die Daten enthalten, mit diesem Konverter durchgeführt werden sollen, ist es wahrscheinlich am bequemsten, die Einheitenregistrierung zu verwenden. Wir registrieren einen Konverter mit der Einheitenregistrierung und plotten Daten mit dem kürzeren Datumsformatter.

```python
import datetime
import matplotlib.units as munits

converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, figsize=(6, 6), layout='constrained')
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```

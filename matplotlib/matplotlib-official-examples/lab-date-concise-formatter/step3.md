# Registering a Converter

If all calls to axes that have dates are to be made using this converter, it is probably most convenient to use the units registry. We register a converter with the units registry and plot data using the concise date formatter.

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

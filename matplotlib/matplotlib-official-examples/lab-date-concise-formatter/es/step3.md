# Registrar un conversor

Si todas las llamadas a ejes que tienen fechas se deben realizar utilizando este conversor, probablemente sea más conveniente utilizar el registro de unidades. Registramos un conversor con el registro de unidades y graficamos datos utilizando el formateador de fechas conciso.

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

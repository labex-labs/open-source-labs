# Registrando um Conversor

Se todas as chamadas para eixos que possuem datas devem ser feitas usando este conversor, provavelmente é mais conveniente usar o registro de unidades. Registramos um conversor com o registro de unidades e plotamos dados usando o formatador de data conciso.

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

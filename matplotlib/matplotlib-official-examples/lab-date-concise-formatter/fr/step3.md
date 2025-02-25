# Enregistrement d'un convertisseur

Si tous les appels à des axes qui ont des dates doivent être effectués en utilisant ce convertisseur, il est probablement le plus pratique d'utiliser le registre d'unités. Nous enregistrons un convertisseur avec le registre d'unités et traçons des données en utilisant le formateur de date concise.

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
axs[0].set_title('Formateur de date concise')
plt.show()
```

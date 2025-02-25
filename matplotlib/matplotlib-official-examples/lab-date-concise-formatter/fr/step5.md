# Enregistrement d'un convertisseur avec localisation

Nous pouvons également enregistrer un convertisseur avec localisation en passant des arguments clés à `~.dates.ConciseDateConverter` et en enregistrant les types de données que vous utiliserez avec le registre d'unités.

```python
import datetime

formats = ['%y',          # les graduations sont principalement en années
           '%b',     # les graduations sont principalement en mois
           '%d',     # les graduations sont principalement en jours
           '%H:%M',  # heures
           '%H:%M',  # minutes
           '%S.%f', ]  # secondes
# ceux-ci peuvent être les mêmes, sauf décalés d'un niveau....
zero_formats = [''] + formats[:-1]
#...sauf pour les graduations qui sont principalement en heures, dans ce cas, il est agréable d'avoir le format jour-mois
zero_formats[3] = '%d-%b'
offset_formats = ['',
                  '%Y',
                  '%b %Y',
                  '%d %b %Y',
                  '%d %b %Y',
                  '%d %b %Y %H:%M', ]

converter = mdates.ConciseDateConverter(
    formats=formats, zero_formats=zero_formats, offset_formats=offset_formats)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Formateur de date concise enregistré avec un format non par défaut')
plt.show()
```

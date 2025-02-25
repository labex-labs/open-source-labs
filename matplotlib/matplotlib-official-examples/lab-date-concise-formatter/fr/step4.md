# Localisation des formats de date

Les formats de date peuvent être localisés si les formats par défaut ne sont pas souhaitables en manipulant l'une des trois listes de chaînes de caractères. Nous modifions les étiquettes pour qu'elles soient au format "jour mois année", au lieu du format ISO "année mois jour".

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # les graduations sont principalement en années
                         '%b',       # les graduations sont principalement en mois
                         '%d',       # les graduations sont principalement en jours
                         '%H:%M',    # heures
                         '%H:%M',    # minutes
                         '%S.%f', ]  # secondes
    # ces formats sont principalement ceux du niveau au-dessus...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...sauf pour les graduations qui sont principalement en heures, dans ce cas, il est agréable d'avoir
    # le format jour-mois :
    formatter.zero_formats[3] = '%d-%b'

    formatter.offset_formats = ['',
                                '%Y',
                                '%b %Y',
                                '%d %b %Y',
                                '%d %b %Y',
                                '%d %b %Y %H:%M', ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Formateur de date concise')
plt.show()
```

# Réglez l'axe des x et formatez les dates

Pour rendre le graphique plus lisible, nous allons définir les limites de l'axe des x sur les premières et dernières dates de la plage. Nous allons également définir les repères principaux et secondaires sur DayLocator et HourLocator respectivement. Enfin, nous allons formater les dates à l'aide de la fonction DateFormatter. Copiez et collez le code suivant :

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```

# Configurer les localiseurs et les formatteurs principaux et secondaires

Pour centrer les étiquettes entre les graduations, nous devons configurer les localiseurs et les formatteurs principaux et secondaires pour l'axe x. Nous utiliserons la fonction `dates.MonthLocator()` pour définir les localiseurs principaux et secondaires sur le mois et la fonction `dates.DateFormatter()` pour formater les étiquettes des graduations secondaires en abréviation de mois.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 est une légère approximation car les mois ont un nombre différent de jours.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```

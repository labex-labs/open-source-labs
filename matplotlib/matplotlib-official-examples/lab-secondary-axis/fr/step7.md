# Créez plusieurs axes

Nous allons maintenant créer un dernier exemple qui convertit `np.datetime64` en jour de l'année sur l'axe des abscisses et de degrés Celsius à degrés Fahrenheit sur l'axe des ordonnées. Nous allons également ajouter un troisième axe des ordonnées et le placer en utilisant un nombre flottant pour l'argument de position.

```python
dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
         for k in range(240)]
temperature = np.random.randn(len(dates)) * 4 + 6.7
fig, ax = plt.subplots(layout='constrained')

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=70)

def date2yday(x):
    """Convertit un numérotateur de date de matplotlib en jours depuis le 01/01/2018."""
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

def yday2date(x):
    """Retourne un numérotateur de date de matplotlib pour *x* jours après le 01/01/2018."""
    y = x + mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

secax_x = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
secax_x.set_xlabel('yday [2018]')

def celsius_to_fahrenheit(x):
    return x * 1.8 + 32

def fahrenheit_to_celsius(x):
    return (x - 32) / 1.8

secax_y = ax.secondary_yaxis(
    'right', functions=(celsius_to_fahrenheit, fahrenheit_to_celsius))
secax_y.set_ylabel(r'$T\ [^oF]$')

def celsius_to_anomaly(x):
    return (x - np.mean(temperature))

def anomaly_to_celsius(x):
    return (x + np.mean(temperature))

# utilisation d'un nombre flottant pour la position :
secax_y2 = ax.secondary_yaxis(
    1.2, functions=(celsius_to_anomaly, anomaly_to_celsius))
secax_y2.set_ylabel(r'$T - \overline{T}\ [^oC]$')
```

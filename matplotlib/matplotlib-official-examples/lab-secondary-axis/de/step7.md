# Erstellen mehrerer Achsen

Wir werden jetzt ein letztes Beispiel erstellen, bei dem `np.datetime64` auf der x-Achse in das Jahrstag und auf der y-Achse von Celsius in Fahrenheit umgewandelt wird. Wir werden auch eine dritte y-Achse hinzufügen und sie anhand eines Floats für das Positionsargument platzieren.

```python
dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
         for k in range(240)]
temperature = np.random.randn(len(dates)) * 4 + 6.7
fig, ax = plt.subplots(layout='constrained')

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=70)

def date2yday(x):
    """Konvertiert matplotlib datenum in Tage seit 2018-01-01."""
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

def yday2date(x):
    """Gibt ein matplotlib datenum für *x* Tage nach 2018-01-01 zurück."""
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

# Verwendung eines Floats für die Position:
secax_y2 = ax.secondary_yaxis(
    1.2, functions=(celsius_to_anomaly, anomaly_to_celsius))
secax_y2.set_ylabel(r'$T - \overline{T}\ [^oC]$')
```

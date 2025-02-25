# Crear múltiples ejes

Ahora crearemos un ejemplo final que convierte `np.datetime64` a día del año en el eje x y de Celsius a Fahrenheit en el eje y. También agregaremos un tercer eje y y lo colocaremos usando un flotante para el argumento de ubicación.

```python
dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
         for k in range(240)]
temperature = np.random.randn(len(dates)) * 4 + 6.7
fig, ax = plt.subplots(layout='constrained')

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=70)

def date2yday(x):
    """Convertir datenum de matplotlib a días desde 2018-01-01."""
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

def yday2date(x):
    """Devolver un datenum de matplotlib para *x* días después de 2018-01-01."""
    y = x + mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

secax_x = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
secax_x.set_xlabel('día del año [2018]')

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

# uso de un flotante para la posición:
secax_y2 = ax.secondary_yaxis(
    1.2, functions=(celsius_to_anomaly, anomaly_to_celsius))
secax_y2.set_ylabel(r'$T - \overline{T}\ [^oC]$')
```

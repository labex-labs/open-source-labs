# Plotten

Dieser Schritt zeigt, wie die Epoche das Plotten beeinflusst. Mit der alten Standardeinstellung der Epoche wurden die Zeiten während der internen `date2num`-Konvertierung aufgerundet, was zu Sprüngen in den Daten führte.

```python
mdates.set_epoch('0000-12-31T00:00:00')

x = np.arange('2000-01-01T00:00:00.0', '2000-01-01T00:00:00.000100', dtype='datetime64[us]')
xold = np.array([mdates.num2date(mdates.date2num(d)) for d in x])
y = np.arange(0, len(x))

fig, ax = plt.subplots(layout='constrained')
ax.plot(xold, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```

Für Daten, die mit der neueren Epoche geplottet werden, ist der Plot glatt:

```python
mdates.set_epoch('1970-01-01T00:00:00')

fig, ax = plt.subplots(layout='constrained')
ax.plot(x, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```

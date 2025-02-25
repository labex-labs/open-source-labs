# Erstellen des Plots

Wir werden einen Plot mit Matplotlib erstellen. Wir werden eine Instanz `d` der Klasse `DataDisplayDownsampler` mit xdata und ydata erstellen. Wir werden eine Figur und eine Achse mit der subplots-Funktion erstellen. Wir werden die Linie verbinden und die Autoskalierung auf False setzen. Wir werden für das Ändern der Anzeigegrenzen verbinden, die x-Begrenzung einstellen und den Plot anzeigen.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```

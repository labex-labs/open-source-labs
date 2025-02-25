# Erstellen der sekundären Y-Achse

Wir werden ein drittes Beispiel erstellen, bei dem die Achsen in einer Transformierung zusammenhängen, die von den Daten ad-hoc und empirisch abgeleitet ist. In diesem Fall werden wir die Vorwärts- und Umkehrtransformationsfunktionen als lineare Interpolation von einem Datensatz zu einem anderen festlegen.

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# gefälschter Datensatz, der die x-Koordinate mit einer anderen datenabgeleiteten Koordinate in Verbindung bringt.
# xnew muss monoton sein, also sortieren wir...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```

# Zweite Reihe um 3 verschieben

In einigen Fällen möchten wir die Fehlerbalken-Untersampling auf verschiedene Teile unserer Daten anwenden. Wir können dies tun, indem wir ein Tupel für den `errorevery`-Parameter angeben. Beispielsweise wenden wir die Fehlerbalken-Untersampling auf die zweite Reihe an, verschieben sie jedoch um 3 Datenpunkte.

```python
fig, ax = plt.subplots()

ax.set_title('Zweite Reihe um 3 verschoben')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```

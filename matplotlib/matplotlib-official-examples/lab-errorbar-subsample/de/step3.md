# Jedes 6. Fehlerbalken unterproben

Lassen Sie uns nun die Fehlerbalken-Untersampling anwenden, um nur jedes 6. Fehlerbalken zu plotten. Wir können dies tun, indem wir das `errorevery`-Parameter der `errorbar`-Funktion verwenden.

```python
fig, ax = plt.subplots()

ax.set_title('Jedes 6. Fehlerbalken')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```

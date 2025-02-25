# Alle Fehlerbalken plotten

Als nächstes werden wir alle Fehlerbalken mit der `errorbar`-Funktion ohne Unterprobenahme plotten. Dies wird als unsere Referenzgrafik dienen.

```python
fig, ax = plt.subplots()

ax.set_title('Alle Fehlerbalken')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```

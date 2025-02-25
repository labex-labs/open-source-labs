# Erzeuge den Plot

Jetzt, wo wir unsere Daten haben, können wir unseren Plot erstellen. Wir beginnen, indem wir ein Achsenobjekt mit `matplotlib.pyplot.subplots()` erstellen. Anschließend werden wir unseren ersten Datensatz auf diesem Achsenobjekt plotten und die Label-Farbe auf rot setzen.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Als nächstes werden wir ein zweites Achsenobjekt instanziieren, das die gleiche x-Achse wie das erste Achsenobjekt teilt, indem wir die `ax1.twinx()`-Methode verwenden. Anschließend werden wir unseren zweiten Datensatz auf diesem neuen Achsenobjekt plotten und die Label-Farbe auf blau setzen.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Schließlich werden wir das Layout unseres Plots mit der `fig.tight_layout()`-Methode anpassen und es mit `matplotlib.pyplot.show()` anzeigen.

```python
fig.tight_layout()
plt.show()
```

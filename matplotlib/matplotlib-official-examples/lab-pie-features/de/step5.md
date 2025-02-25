# Die Farben anpassen

Wir können die Farben der Sektoren anpassen, indem wir eine Liste von Farben an den `colors`-Parameter der `pie()`-Funktion übergeben.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```

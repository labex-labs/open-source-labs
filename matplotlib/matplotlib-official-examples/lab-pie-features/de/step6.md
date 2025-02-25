# Die Schraffierungsmuster anpassen

Wir können die Schraffierungsmuster der Sektoren anpassen, indem wir eine Liste von Schraffierungsmustern an den `hatch`-Parameter der `pie()`-Funktion übergeben.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```

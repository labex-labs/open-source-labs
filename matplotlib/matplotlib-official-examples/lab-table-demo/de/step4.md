# Erstellen eines Farbschemas

Wir werden ein Farbschema für die Tabelle mit der Funktion `plt.cm.BuPu` erstellen. Wir werden für die Zeilen eine pastellblaue und -violette Farbe verwenden.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```

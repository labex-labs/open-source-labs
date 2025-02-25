# Diagramm erstellen

Wir können jetzt ein Diagramm mit `matplotlib` erstellen und das `LineCollection`-Objekt mit der `add_collection`-Methode des `Axes`-Objekts zum Diagramm hinzufügen.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```

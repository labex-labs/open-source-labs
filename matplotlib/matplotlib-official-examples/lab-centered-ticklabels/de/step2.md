# Erzeuge den Graphen

Als nächstes werden wir den Graphen mit der `subplots()`-Funktion von Matplotlib erstellen und den angepassten Schließungspreis von Google-Aktien im Laufe der Zeit darstellen.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```

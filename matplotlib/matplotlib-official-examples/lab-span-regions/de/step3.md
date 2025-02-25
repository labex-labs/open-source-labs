# Den Graphen erstellen

Jetzt werden wir den Graphen mit `matplotlib.pyplot` erstellen. Wir werden die Sinuswelle plotten und eine horizontale Linie bei y = 0 hinzufügen.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```

# Das Diagramm erstellen

Jetzt werden wir das Diagramm mit der Bibliothek `matplotlib.pyplot` erstellen. Wir werden die x- und y-Bereiche des Diagramms festlegen und dann die Daten plotten.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```

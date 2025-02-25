# Erzeuge die Figur und die Achsen

In diesem Schritt wirst du die Figur und die Achsen für das Diagramm erstellen. Du wirst auch die Position der Achsen anpassen, um Platz für die Schieberegler zu schaffen.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```

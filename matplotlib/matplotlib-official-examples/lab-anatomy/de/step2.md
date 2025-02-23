# Figur erstellen und Achsen einrichten

Als nächstes werden wir eine Figur erstellen und die Achsen einrichten. Wir werden die Methode `add_axes()` verwenden, um eine neue Achsenmenge innerhalb der Figur zu erstellen. Wir werden auch Grenzen für die x- und y-Achsen setzen und Rasterlinien hinzufügen.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```

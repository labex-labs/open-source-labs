# Einen gekrümmten Linienzug mit markierten Pfadeffekten zeichnen

Wir werden nun einen gekrümmten Linienzug mit markierten Pfadeffekten zeichnen.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

# Grenzen festlegen und Markierungen entfernen

In diesem Schritt werden wir die y-Grenze festlegen und die Markierungen aus dem Diagramm entfernen.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```

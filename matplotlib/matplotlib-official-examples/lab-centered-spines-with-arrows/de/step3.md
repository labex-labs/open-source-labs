# Verschieben der Achsenlinien (Spines)

Standardmäßig werden die Achsenlinien (Spines) am Rand des Diagramms gezeichnet. In diesem Fall möchten Sie die linke und die untere Achsenlinie in die Mitte des Diagramms verschieben.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```

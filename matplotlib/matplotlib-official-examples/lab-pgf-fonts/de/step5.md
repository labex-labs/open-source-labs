# Hinzufügen von Text zum Diagramm

Wir werden Text zum Diagramm mit der Funktion `ax.text()` hinzufügen. Wir werden Text an vier verschiedene Stellen auf dem Diagramm hinzufügen, wobei jede Stelle eine andere Schriftfamilie hat: Serif, Monospace, Sans-Serif und Kurrent.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```

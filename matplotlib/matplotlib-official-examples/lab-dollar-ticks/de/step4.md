# Anpassen der Teilstriche (Ticks)

Wir können auch die Parameter der Teilstriche anpassen, um das Erscheinungsbild unseres Diagramms weiter zu verbessern. In diesem Beispiel werden wir die Farbe der Teilstrichenbeschriftungen auf Grün ändern und sie auf die rechte Seite des Diagramms verschieben.

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

Im obigen Code verwenden wir die Methode `tick_params`, um die Parameter der Teilstriche auf der y-Achse anzupassen. Wir setzen den Parameter `axis` auf `'y'`, um anzugeben, dass wir die y-Achse anpassen, und den Parameter `which` auf `'major'`, um anzugeben, dass wir die Haupteinteilungen anpassen. Wir setzen den Parameter `labelcolor` auf `'green'`, um die Farbe der Teilstrichenbeschriftungen zu ändern, und den Parameter `labelright` auf `True`, um die Teilstrichenbeschriftungen auf die rechte Seite des Diagramms zu verschieben.

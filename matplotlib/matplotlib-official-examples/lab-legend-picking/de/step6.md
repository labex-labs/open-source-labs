# Definieren der Funktion für das Auslöseereignis beim Auswählen

Wir werden die Funktion für das Auslöseereignis beim Auswählen definieren, die die Sichtbarkeit der ursprünglichen Linie entsprechend der Legendenproxy-Linie umschaltet.

```python
def on_pick(event):
    # Beim Auslöseereignis beim Auswählen finde die ursprüngliche Linie,
    # die der Legendenproxy-Linie entspricht, und umschalte ihre Sichtbarkeit.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Ändere die Alpha-Eigenschaft der Linie in der Legende, damit wir sehen können,
    # welche Linien umgeschaltet wurden.
    legline.set_alpha(1.0 wenn sichtbar else 0.2)
    fig.canvas.draw()
```

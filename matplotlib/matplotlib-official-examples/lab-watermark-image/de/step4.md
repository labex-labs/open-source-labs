# Bild überlagern

Um das Bild auf das Diagramm zu legen, können wir die Methode `figimage` aus der Klasse `matplotlib.figure.Figure` verwenden. Wir müssen das Bild, die Position des Bildes auf dem Diagramm, die z-Reihenfolge (um das Bild nach vorne zu bringen) und den Alpha-Wert (um das Bild halbtransparent zu machen) angeben.

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```

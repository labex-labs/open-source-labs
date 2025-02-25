# Aktualisierung der Daten

Wir werden eine Methode `update` definieren, die die Daten aktualisiert. Die Methode wird die ax (Achse) als Eingabeparameter entgegennehmen. Wir werden die Linie aktualisieren, indem wir die Anzeigegrenze erhalten und überprüfen, ob die Breite der Anzeigegrenze von delta unterschiedlich ist. Wenn die Breite der Anzeigegrenze von delta unterschiedlich ist, werden wir delta aktualisieren und xstart und xend erhalten. Wir werden dann die Daten auf die aufniedergeschlüsselten Daten setzen und das Leerlaufzeichen zeichnen.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```

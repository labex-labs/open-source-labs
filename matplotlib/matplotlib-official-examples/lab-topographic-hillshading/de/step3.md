# Festlegen der Zellengröße

Wenn Sie eine topografisch genaue vertikale Vergrößerung benötigen oder nicht raten möchten, was der Wert von `vert_exag` sein sollte, müssen Sie die Zellengröße des Gitters angeben (d.h. die Parameter `dx` und `dy`). Andernfalls wird jeder von Ihnen angegebene `vert_exag`-Wert relativ zum Gitterschrittweite Ihrer Eingabedaten sein. In diesem Schritt berechnen wir die `dx`- und `dy`-Werte in Metern.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```

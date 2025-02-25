# Das Hervorheben von Bereichen einer Achse mit `axhspan` und `axvspan`

Ein weiterer praktischer Gebrauch von gefüllten Bereichen ist das Hervorheben horizontaler oder vertikaler Bereiche einer Achse. Dazu hat Matplotlib die Hilfsfunktionen `axhspan` und `axvspan`. Weitere Informationen finden Sie in der `axhspan_demo`-Galerie.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```

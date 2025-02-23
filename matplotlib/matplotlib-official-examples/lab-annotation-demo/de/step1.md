# Angabe von Textpunkten und Annotationspunkten

Sie müssen einen Annotationspunkt `xy=(x, y)` angeben, um diesen Punkt zu annotieren. Darüber hinaus können Sie für die Position des Texts für diese Annotation einen Textpunkt `xytext=(x, y)` angeben. Optional können Sie das Koordinatensystem von `xy` und `xytext` mit einem der folgenden Strings für `xycoords` und `textcoords` angeben (Standard ist 'data'):

- 'figure points' : Punkte vom unteren linken Eck des Diagramms
- 'figure pixels' : Pixel vom unteren linken Eck des Diagramms
- 'figure fraction' : (0, 0) ist das untere linke Eck des Diagramms und (1, 1) ist das obere rechte
- 'axes points' : Punkte vom unteren linken Eck der Achsen
- 'axes pixels' : Pixel vom unteren linken Eck der Achsen
- 'axes fraction' : (0, 0) ist das untere linke Eck der Achsen und (1, 1) ist das obere rechte
- 'offset points' : Geben Sie einen Offset (in Punkten) von dem xy-Wert an
- 'offset pixels' : Geben Sie einen Offset (in Pixeln) von dem xy-Wert an
- 'data' : Verwenden Sie das Achsendaten-Koordinatensystem

Hinweis: Für physikalische Koordinatensysteme (Punkte oder Pixel) ist der Ursprung der (untere, linke) Rand des Diagramms oder der Achsen.

Optional können Sie Pfeilarrow-Eigenschaften angeben, die einen Pfeil von dem Text zum annotierten Punkt zeichnen, indem Sie ein Wörterbuch mit Pfeilarrow-Eigenschaften angeben. Gültige Schlüssel sind:

- `width`: die Breite des Pfeils in Punkten
- `frac`: der Anteil der Pfeillänge, der vom Kopf eingenommen wird
- `headwidth`: die Breite der Basis des Pfeilkopfes in Punkten
- `shrink`: bewegen Sie die Spitze und die Basis um einen gewissen Prozentsatz von dem annotierten Punkt und dem Text weg
- `jeder Schlüssel für matplotlib.patches.polygon` (z.B. facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Erstellen Sie unser Diagramm und die Daten, die wir zum Plotten verwenden
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plotten Sie eine Linie und fügen Sie einige einfache Annotations hinzu
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025,.975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# Die folgenden Beispiele zeigen, wie diese Pfeile gezeichnet werden.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# Sie können auch negative Punkte oder Pixel verwenden, um von (rechts, oben) anzugeben.
# Beispielsweise ist (-10, 10) 10 Punkte links von der rechten Seite der Achsen und 10
# Punkte über der unteren Seite

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```

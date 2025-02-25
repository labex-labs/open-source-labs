# Definiere ein Dreieck, indem du drei Punkte anklickst

In diesem Schritt werden wir ein Dreieck definieren, indem wir drei Punkte anklicken. Dazu verwenden wir die Funktionen `ginput` und `waitforbuttonpress`. Die `ginput`-Funktion ermöglicht es uns, Punkte auf dem Diagramm mit der Maus auszuwählen, und die `waitforbuttonpress`-Funktion wartet auf einen Button-Events.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('Du wirst ein Dreieck definieren, klicke, um zu beginnen')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Wähle 3 Ecken mit der Maus')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Zu wenige Punkte, starte von vorne')
            time.sleep(1)  # Warte eine Sekunde

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Sind Sie zufrieden? Klicken Sie auf die Taste für Ja, auf die Maus für Nein')

    if plt.waitforbuttonpress():
        break

    # Entferne die Füllung
    for p in ph:
        p.remove()
```

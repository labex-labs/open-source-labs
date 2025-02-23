# Kopfform im Anzeigeraum fix, Ankerpunkte im Datenraum fix

Dies ist nützlich, wenn Sie einen Graphen annotieren und den Pfeil nicht verändern möchten, wenn Sie den Graphen verschieben oder skalieren.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_tail = 0.1
y_tail = 0.5
x_head = 0.9
y_head = 0.8
dx = x_head - x_tail
dy = y_head - y_tail

fig, axs = plt.subplots(nrows=2)
arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100)
axs[0].add_patch(arrow)

arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100)
axs[1].add_patch(arrow)
axs[1].set(xlim=(0, 2), ylim=(0, 2))

plt.show()
```

# Ein quadratisches Achsenbild unabhängig von den Daten

Wir werden ein quadratisches Achsenbild erzeugen, unabhängig davon, was die Datengrenzen sind.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

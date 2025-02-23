# Un axe carré, indépendant des données

Nous allons produire un axe carré, peu importent les limites des données.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

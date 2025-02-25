# Квадратная ось, независимая от данных

Мы создадим квадратную ось, независимо от ограничений данных.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

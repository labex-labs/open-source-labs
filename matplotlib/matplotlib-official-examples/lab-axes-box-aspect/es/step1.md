# Un eje cuadrado, independiente de los datos

Vamos a crear un eje cuadrado, sin importar cuáles sean los límites de los datos.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

# Importar Bibliotecas e Criar uma Figura

O primeiro passo é importar as bibliotecas necessárias e criar uma figura. Usamos o módulo `matplotlib.pyplot` para criar uma figura e o módulo `mpl_toolkits.axes_grid1` para criar espaço para o rótulo do eixo y.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```

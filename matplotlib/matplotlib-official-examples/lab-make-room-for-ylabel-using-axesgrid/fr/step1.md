# Importation des bibliothèques et création d'une figure

La première étape consiste à importer les bibliothèques nécessaires et à créer une figure. Nous utilisons le module `matplotlib.pyplot` pour créer une figure et le module `mpl_toolkits.axes_grid1` pour laisser de la place pour l'étiquette y.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```

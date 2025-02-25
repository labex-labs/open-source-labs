# Importez les bibliothèques et les données nécessaires

Nous devons tout d'abord importer les bibliothèques et les données nécessaires pour créer notre grille. Nous utiliserons `matplotlib.pyplot` pour tracer, `cbook` pour obtenir un ensemble de données d'échantillonnage et `ImageGrid` pour créer notre grille.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Obtenez des données d'échantillonnage
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # Tableau 15x15
extent = (-3, 4, -4, 3)
```

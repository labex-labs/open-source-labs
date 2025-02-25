# Importieren von erforderlichen Bibliotheken und Daten

Wir müssen zunächst die erforderlichen Bibliotheken und Daten importieren, um unser Gitter zu erstellen. Wir werden `matplotlib.pyplot` zum Zeichnen, `cbook` verwenden, um einen Beispiel-Datensatz zu erhalten, und `ImageGrid` verwenden, um unser Gitter zu erstellen.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```

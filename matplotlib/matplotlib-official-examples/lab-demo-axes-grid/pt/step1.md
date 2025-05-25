# Importar bibliotecas e dados necessários

Primeiramente, precisamos importar as bibliotecas e os dados necessários para criar nossa grade. Usaremos `matplotlib.pyplot` para plotagem, `cbook` para obter um conjunto de dados de exemplo e `ImageGrid` para criar nossa grade.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```

# Preparação do Conjunto de Dados

Começamos gerando o conjunto de dados S-curve.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

# importação não utilizada, mas necessária para fazer projeções 3D com matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
```

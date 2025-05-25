# Importar as bibliotecas necessárias e fixar o estado aleatório

Primeiramente, precisamos importar as bibliotecas necessárias e fixar o estado aleatório para reprodutibilidade. Usaremos `numpy` para gerar alguns dados aleatórios, `matplotlib.pyplot` para criar visualizações e `cm` de `matplotlib` para definir os mapas de cores (color maps).

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```

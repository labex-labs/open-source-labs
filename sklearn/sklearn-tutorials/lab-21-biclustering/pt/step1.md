# Importar bibliotecas e conjunto de dados necessários

Primeiro, vamos importar as bibliotecas necessárias e carregar um conjunto de dados de amostra que usaremos para o biclustering.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Carregar dados de amostra
data = np.arange(100).reshape(10, 10)
```

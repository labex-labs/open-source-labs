# Gerar Dados de Amostra

Neste passo, geramos dados de amostra utilizando um processo altamente não-gaussiano, 2 distribuições t de Student com um baixo número de graus de liberdade.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Misturar dados
A = np.array([[1, 1], [0, 2]])  # Matriz de mistura

X = np.dot(S, A.T)  # Gerar observações
```

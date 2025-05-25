# Geração de Dados

Geramos dois componentes (cada um contendo `n_samples`) amostrando aleatoriamente a distribuição normal padrão, como retornado por `numpy.random.randn`. Um componente é mantido esférico, mas deslocado e redimensionado. O outro é deformado para ter uma matriz de covariância mais geral.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # general
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # spherical

X = np.concatenate([component_1, component_2])
```

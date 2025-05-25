# Gerar o Conjunto de Dados Swiss Roll

Começamos gerando o conjunto de dados Swiss Roll usando a função `make_swiss_roll()` de `sklearn.datasets`. Esta função gera um conjunto de dados 3D com forma de espiral.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```

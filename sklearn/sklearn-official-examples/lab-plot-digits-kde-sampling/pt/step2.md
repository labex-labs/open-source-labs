# Otimizar a Largura de Banda

Utilizamos a validação cruzada por busca em grade para otimizar o parâmetro de largura de banda do KDE. O parâmetro de largura de banda controla a suavidade da estimativa de densidade.

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# usar validação cruzada por busca em grade para otimizar a largura de banda
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("melhor largura de banda: {0}".format(grid.best_estimator_.bandwidth))

# usar o melhor estimador para calcular a estimativa de densidade do kernel
kde = grid.best_estimator_
```

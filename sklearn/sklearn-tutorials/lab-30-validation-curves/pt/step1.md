# Importar as Bibliotecas Necessárias e Carregar os Dados

Vamos começar importando as bibliotecas necessárias e carregando um conjunto de dados. Neste exemplo, usaremos o conjunto de dados Iris.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```

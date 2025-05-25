# Carregar o Conjunto de Dados de Diabetes

Começamos carregando o conjunto de dados de diabetes do scikit-learn e selecionando apenas um recurso do conjunto de dados.

```python
import numpy as np
from sklearn import datasets

# Carregar o conjunto de dados de diabetes
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Usar apenas um recurso
diabetes_X = diabetes_X[:, np.newaxis, 2]
```

# Importação de bibliotecas necessárias e carregamento de dados

Começaremos importando as bibliotecas necessárias e carregando o conjunto de dados de dígitos do scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# carregar o conjunto de dados de dígitos
X, y = load_digits(return_X_y=True, n_class=3)
```

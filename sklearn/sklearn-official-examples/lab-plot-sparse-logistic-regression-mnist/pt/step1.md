# Importar Bibliotecas

Começaremos importando as bibliotecas necessárias para este laboratório. Usaremos a biblioteca scikit-learn para obter o conjunto de dados, treinar o modelo e avaliar o desempenho do modelo.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```

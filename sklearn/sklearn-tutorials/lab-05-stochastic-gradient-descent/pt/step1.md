# Importar as bibliotecas necessárias

Primeiro, precisamos importar as bibliotecas necessárias. Usaremos a biblioteca scikit-learn para aprendizado de máquina e pré-processamento de dados.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```

# Carregar e pré-processar os dados

Começaremos carregando o conjunto de dados de dígitos manuscritos do scikit-learn e dividindo-o em conjuntos de treino e teste. Também escalaremos os dados para ter média zero e variância unitária.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar o conjunto de dados de dígitos
X, y = datasets.load_digits(return_X_y=True)

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar os dados para ter média zero e variância unitária
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

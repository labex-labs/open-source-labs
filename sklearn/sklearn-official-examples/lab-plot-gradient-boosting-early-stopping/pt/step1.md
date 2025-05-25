# Carregar as Bibliotecas e Dados Necessários

Primeiro, precisamos carregar as bibliotecas e os dados necessários. Usaremos a biblioteca scikit-learn para a implementação do boosting de gradientes.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_list = [
    datasets.load_iris(return_X_y=True),
    datasets.make_classification(n_samples=800, random_state=0),
    datasets.make_hastie_10_2(n_samples=2000, random_state=0),
]
names = ["Dados Iris", "Dados de Classificação", "Dados de Hastie"]
n_estimators = 200
```

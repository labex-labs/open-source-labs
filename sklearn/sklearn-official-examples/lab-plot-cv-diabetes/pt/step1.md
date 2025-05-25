# Carregar e preparar o conjunto de dados

Primeiro, carregaremos e prepararemos o conjunto de dados de diabetes. Apenas usaremos as primeiras 150 amostras neste exercício.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```

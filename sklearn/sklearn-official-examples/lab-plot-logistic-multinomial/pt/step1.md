# Importar Bibliotecas

Começaremos importando as bibliotecas necessárias para este laboratório. Usaremos a biblioteca scikit-learn para gerar o conjunto de dados e treinar os modelos de regressão logística, e a biblioteca matplotlib para plotar a fronteira de decisão.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```

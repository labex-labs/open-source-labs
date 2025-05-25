# Importação do Pacote Python e do Conjunto de Dados, Carregamento do Conjunto de Dados

```python
# Importações científicas padrão do Python
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Importação de conjuntos de dados, classificadores e métricas de desempenho
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# Conjunto de dados dígitos
digits = datasets.load_digits(n_class=9)
```

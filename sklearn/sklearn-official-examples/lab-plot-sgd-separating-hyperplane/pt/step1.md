# Importar bibliotecas necessárias e gerar dados

Primeiro, precisamos importar as bibliotecas necessárias e gerar um conjunto de dados adequado para classificação. Neste exemplo, geraremos 50 pontos separáveis usando a função `make_blobs` do Scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# criamos 50 pontos separáveis
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```

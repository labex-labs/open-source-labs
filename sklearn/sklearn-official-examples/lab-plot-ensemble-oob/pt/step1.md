# Importação de Bibliotecas Necessárias

Começaremos importando as bibliotecas necessárias, incluindo scikit-learn, NumPy e Matplotlib. Também definiremos um valor de estado aleatório para garantir a reprodutibilidade.

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```

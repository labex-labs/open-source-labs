# Carregar o conjunto de dados

Primeiro, precisamos carregar o conjunto de dados de dígitos do scikit-learn e dividi-lo em características e rótulos.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```

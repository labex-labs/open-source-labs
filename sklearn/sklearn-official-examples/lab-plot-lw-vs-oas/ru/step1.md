# Импорт библиотек

Во - первых, нам нужно импортировать необходимые библиотеки для этой лабораторной работы. Мы будем использовать `numpy` для численных вычислений, `matplotlib` для визуализации и `scikit - learn` для оценки ковариации.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```

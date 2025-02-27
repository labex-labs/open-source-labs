# Импорт библиотек

В этом шаге мы импортируем необходимые библиотеки для нашего анализа. Мы импортируем библиотеку scikit-learn для машинного обучения, numpy для численного вычисления и matplotlib для визуализации.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```

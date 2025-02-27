# Импорт необходимых библиотек

Сначала нам нужно импортировать необходимые библиотеки, в том числе `MLPClassifier`, `MinMaxScaler`, `datasets` и `matplotlib.pyplot`. Мы также импортируем `ConvergenceWarning`, чтобы игнорировать предупреждения о неконвергенции во время обучения.

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```

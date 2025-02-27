# Импорт библиотек

Начнем с импорта необходимых библиотек для этого практического занятия. Мы будем использовать библиотеку scikit-learn для получения набора данных, обучения модели и оценки ее производительности.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```

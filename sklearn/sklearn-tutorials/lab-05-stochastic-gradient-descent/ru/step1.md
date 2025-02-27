# Импортируем необходимые библиотеки

Сначала нам нужно импортировать необходимые библиотеки. Мы будем использовать библиотеку scikit - learn для машинного обучения и предобработки данных.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```

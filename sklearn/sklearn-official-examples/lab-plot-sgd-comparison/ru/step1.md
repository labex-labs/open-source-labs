# Загрузка и предобработка данных

Начнем с загрузки набора данных рукописных цифр из scikit-learn и разделения его на обучающий и тестовый наборы. Также масштабируем данные, чтобы они имели нулевое среднее и единичную дисперсию.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загрузка набора данных digits
X, y = datasets.load_digits(return_X_y=True)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабирование данных, чтобы они имели нулевое среднее и единичную дисперсию
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

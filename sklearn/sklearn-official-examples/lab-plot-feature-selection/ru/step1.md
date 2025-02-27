# Генерация выборочных данных

Сначала мы сгенерируем некоторые выборочные данные для демонстрации. Мы будем использовать набор данных iris и добавить к нему некоторое количество шумовых данных, не связанных между собой.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Набор данных iris
X, y = load_iris(return_X_y=True)

# Некоторые шумовые данные, не связанные между собой
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Добавляем шумовые данные к информативным признакам
X = np.hstack((X, E))

# Разделяем набор данных на выборочный и тестовый наборы для выбора признаков и оценки классификатора
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```

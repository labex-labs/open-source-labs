# Генерация данных

Первым шагом является генерация некоторых примеров данных, которые мы можем использовать для обучения и тестирования нашей модели. Мы будем использовать функцию `make_classification` из модуля `sklearn.datasets` для генерации случайной задачи бинарной классификации с 3 информативными признаками.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```

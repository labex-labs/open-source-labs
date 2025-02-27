# Импортируем необходимые библиотеки и определяем константы

Сначала нам нужно импортировать необходимые библиотеки и определить цвета и константу случайного зерна для генерации мультиметкажного датасета.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # красный
        "#0198E1",  # синий
        "#BF5FFF",  # фиолетовый
        "#FCD116",  # желтый
        "#FF7216",  # оранжевый
        "#4DBD33",  # зеленый
        "#87421F",  # коричневый
    ]
)

# Используем одно и то же случайное зерно для нескольких вызовов make_multilabel_classification,
# чтобы гарантировать одинаковые распределения
RANDOM_SEED = np.random.randint(2**10)
```

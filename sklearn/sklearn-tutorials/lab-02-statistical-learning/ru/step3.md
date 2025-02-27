# Объекты оценщиков

Объекты оценщиков в scikit-learn используются для обучения на данных и для предсказания. Это могут быть алгоритмы классификации, регрессии или кластеризации, или трансформеры, которые извлекают полезные признаки из исходных данных. Создадим простой пример объекта оценщика:

```python
from sklearn.base import BaseEstimator

class Estimator(BaseEstimator):
    def __init__(self, param1=0, param2=0):
        self.param1 = param1
        self.param2 = param2

    def fit(self, data):
        # Реализация метода fit
        pass

estimator = Estimator()
```

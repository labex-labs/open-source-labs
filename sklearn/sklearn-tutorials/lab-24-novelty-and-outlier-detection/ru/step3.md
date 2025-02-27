# Создаем оценщик для обнаружения выбросов

Теперь мы можем создать объект оценщика для обнаружения выбросов из класса `neighbors.LocalOutlierFactor`. Этот класс реализует алгоритм Local Outlier Factor, который является популярным методом для обнаружения выбросов.

```python
estimator = neighbors.LocalOutlierFactor()
```

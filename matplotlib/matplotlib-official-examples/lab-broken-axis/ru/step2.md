# Создание данных

Теперь создадим некоторые случайные данные, которые будут содержать выбросы. Мы будем использовать `numpy.random.rand` для генерации 30 случайных чисел, а затем добавим два выброса в данные.

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Теперь создадим два выброса, которые находятся далеко от остальных точек.
pts[[3, 14]] +=.8
```

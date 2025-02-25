# Методы универсальных функций

Универсальные функции имеют четыре метода: reduce, accumulate, reduceat и outer. Эти методы полезны для выполнения операций над массивами. Посмотрим на метод reduce.

```python
import numpy as np

# Создаем массив
arr = np.arange(9).reshape(3, 3)

# Сворачиваем массив вдоль первой оси
result = np.add.reduce(arr, 1)

# Выводим результат
print(result)
```

Результат:

```
array([ 3, 12, 21])
```

# Преобразуйте строки в числовые типы

Чтобы исправить поведение делений на оси, необходимо преобразовать строки в числовые типы. Вот пример:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

В этом примере мы преобразуем строковые значения в числа с плавающей точкой с использованием `np.asarray()`. При повторном построении графика метки делений на оси расположены как ожидается.

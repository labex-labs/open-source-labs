# Обработка делений на оси с датой и временем

При работе с значениями даты и времени на оси x важно преобразовать строки в объекты datetime, чтобы получить правильные локаторы и форматировщики дат. Вот пример:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

В этом примере мы преобразуем строковые значения в datetime64 с использованием `np.asarray()`. При повторном построении графика метки делений на оси расположены как ожидается.

# Обработка избыточного количества делений на оси

Если на оси x есть много элементов, все они являются строками, то мы можем получить слишком много делений, которые не читаются. В этом случае необходимо преобразовать строки в числовые типы. Вот пример:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Categories')
plt.show()
```

В этом примере на оси x есть 100 строковых значений, что приводит к слишком большому количеству делений, которые не читаются.

Чтобы исправить это, необходимо преобразовать строки в числа с плавающей точкой. Вот пример:

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with 100 elements
x = [f'{xx}' for xx in np.arange(100)]
y = np.arange(100)

# convert strings to floats
x = np.asarray(x, float)

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Floats')
plt.show()
```

В этом примере мы преобразуем строковые значения в числа с плавающей точкой с использованием `np.asarray()`. При повторном построении графика метки делений на оси расположены как ожидается.

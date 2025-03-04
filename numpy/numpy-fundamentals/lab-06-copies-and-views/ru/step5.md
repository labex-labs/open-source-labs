# Другие операции

В NumPy есть другие операции, которые могут создавать представления или копии.

- Функция `reshape()` создает представление, если это возможно, или копию в противном случае. Например:

```python
import numpy as np

# Создать массив
x = np.ones((2, 3))

# Транспонировать массив
y = x.T

# Попытка изменить форму массива
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

В приведенном выше примере массив `y` становится не непрерывным после транспонирования, поэтому изменение его формы требует копирования.

- Функция `ravel()` возвращает непрерывное сглаженное представление массива, если это возможно. С другой стороны, метод `flatten()` всегда возвращает сглаженную копию массива. Например:

```python
import numpy as np

# Создать массив
x = np.arange(9).reshape(3, 3)

# Создать сглаженное представление
y = x.ravel()

# Создать сглаженную копию
z = x.flatten()

# Распечатать исходный массив
print(x)  # Вывод: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

В приведенном выше примере `y` - это представление, а `z` - копия.

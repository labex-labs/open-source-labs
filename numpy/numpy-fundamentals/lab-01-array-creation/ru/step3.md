# Копирование, объединение или изменение существующих массивов

После создания массивов вы можете скопировать, объединить или изменить их, чтобы создать новые массивы. При присвоении массива или его элементов новой переменной используйте функцию `np.copy`, чтобы создать новый массив, а не представление (view) на исходный массив. Вот пример:

```python
import numpy as np

# Создать массив
a = np.array([1, 2, 3, 4])

# Создать представление первых двух элементов массива
b = a[:2]

# Изменить представление
b += 1

# Распечатать исходный массив и измененное представление
print('a =', a, '; b =', b)
```

Для объединения массивов вы можете использовать функции, такие как `np.vstack`, `np.hstack` и `np.block`. Вот пример объединения четырех массивов размером 2x2 в массив размером 4x4 с использованием `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```

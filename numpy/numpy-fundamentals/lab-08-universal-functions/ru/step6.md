# Переопределение поведения универсальной функции

Классы, в том числе и подклассы ndarray, могут переопределить, как универсальные функции (ufuncs) действуют на них, определяя определенные специальные методы. Это позволяет настроить поведение ufunc. Посмотрим на пример.

```python
import numpy as np

# Определяем пользовательский класс
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# Создаем экземпляр пользовательского класса
arr = MyArray([1, 2, 3])

# Выполняем сложение
result = arr + 1

# Выводим результат
print(result)
```

Результат:

```
Custom add method called
[2 3 4]
```

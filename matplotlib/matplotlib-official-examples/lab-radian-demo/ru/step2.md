# Создать данные

Создайте массив значений от 0 до 15 с шагом 0,01 и преобразуйте их в радианы с использованием функции radians из пакета basic_units.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```

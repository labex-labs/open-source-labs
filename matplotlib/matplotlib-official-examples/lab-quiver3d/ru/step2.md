# Создание сетки

Далее мы создадим сетку точек, на которой будем отображать поле векторов. В этом примере мы создадим сетку точек с помощью функции `meshgrid` NumPy. Функция `arange` используется для создания массива равномерно распределенных точек в заданном интервале.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```

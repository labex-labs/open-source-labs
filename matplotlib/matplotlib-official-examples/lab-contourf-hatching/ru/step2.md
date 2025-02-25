# Создаем данные

Далее мы создадим некоторые образцовые данные для построения графика. В этом примере мы создадим 2D-сетку значений x и y и используем их для вычисления значений z.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```

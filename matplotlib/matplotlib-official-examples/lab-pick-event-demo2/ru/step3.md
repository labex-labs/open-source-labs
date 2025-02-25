# Построение графика данных

Теперь мы построим график mu против sigma с использованием модуля pyplot библиотеки Matplotlib. Мы создадим точечный график с использованием вычисленных значений для mu и sigma. Также мы добавим интерактивность к графику, установив параметр `picker` в значение True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```

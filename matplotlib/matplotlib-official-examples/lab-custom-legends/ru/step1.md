# Построение линий

В этом шаге мы построим набор линий с использованием библиотеки Matplotlib. Сначала мы создадим некоторые случайные данные с использованием NumPy. Затем мы установим цикл цветов с использованием функции `cycler`, чтобы указать карту цветов. Наконец, мы построим данные с использованием функции `plot` и вызовем `legend()`, чтобы сгенерировать легенду.

```python
import matplotlib.pyplot as plt
import numpy as np

# Установка случайного состояния для воспроизводимости
np.random.seed(19680801)

# Создание случайных данных
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Установка цикла цветов
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Построение данных и генерация легенды
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```

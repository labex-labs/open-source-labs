# Центрированные координаты

Часто пользователь хочет передать _X_ и _Y_ с одинаковыми размерами, как у _Z_, в `.axes.Axes.pcolormesh`. Это также допустимо, если передать `shading='auto'` (значение по умолчанию, заданное :rc:`pcolor.shading`). До Matplotlib 3.3 `shading='flat'` удалял последний столбец и строку _Z_, но теперь выдаёт ошибку. Если это действительно то, что вы хотите, то просто вручную удалите последнюю строку и столбец _Z_:

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```

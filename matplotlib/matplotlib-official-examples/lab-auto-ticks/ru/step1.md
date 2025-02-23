# Диаграмма рассеяния без режима автоматической настройки делений round_numbers

В этом шаге мы создадим диаграмму рассеяния без режима автоматической настройки делений round_numbers и изучим поведение автоматической настройки делений.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```

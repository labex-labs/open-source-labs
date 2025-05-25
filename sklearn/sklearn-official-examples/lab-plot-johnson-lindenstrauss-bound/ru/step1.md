# Теоретические границы

Первым шагом является исследование теоретических границ леммы Джонсона-Линденштрасса. Мы построим график минимального числа размерностей, необходимых для гарантии `eps`-эмбеддинга для возрастающего числа выборок `n_samples`. Дисторсия，引入的由随机投影 `p` 定义的失真，由以下事实断言：`p` 以高概率定义了一个 `eps`-嵌入，定义如下：

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

где `u` и `v` - любые строки из набора данных формы `(n_samples, n_features)`, а `p` - проекция случайной Гауссовой матрицы `N(0, 1)` формы `(n_components, n_features)` (или разреженная матрица Ахлиоптаса).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# диапазон допустимых искажений
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# диапазон числа выборок (наблюдений) для встраивания
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Число наблюдений для eps-эмбеддинга")
plt.ylabel("Минимальное число размерностей")
plt.title("Границы Джонсона-Линденштрасса:\nn_samples vs n_components")
plt.show()
```

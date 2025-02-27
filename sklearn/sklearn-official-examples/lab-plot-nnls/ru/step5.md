# Сравнение коэффициентов регрессии

Теперь мы сравним коэффициенты регрессии между неотрицательными наименьшими квадратами и классической линейной регрессией. Мы построим график коэффициентов друг против друга и заметим, что они сильно коррелируют. Однако неотрицательное ограничение сужает некоторые коэффициенты до 0. Это происходит потому, что неотрицательные наименьшие квадраты по своей природе дают разреженные результаты.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```

# Создаем график с линейной шкалой

Мы создадим график с линейной шкалой. Это можно сделать, просто построив накопленные функции распределения для нормального, лапласиана и распределения Коши с помощью `plot()` и добавив легенду с помощью `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

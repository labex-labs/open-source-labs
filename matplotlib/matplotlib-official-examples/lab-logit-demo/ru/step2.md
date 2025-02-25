# Создаем график с логит шкалой и стандартной нотацией

Мы создадим график с логит шкалой и стандартной нотацией. Это можно сделать, установив масштаб оси y в логит с помощью `set_yscale("logit")` и установив пределы оси y с помощью `set_ylim()`. Мы также построим накопленные функции распределения для нормального, лапласиана и распределения Коши с помощью `plot()` и добавим легенду с помощью `legend()`.

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

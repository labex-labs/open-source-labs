# Создание стволовой диаграммы

Далее мы создадим стволовую диаграмму с некоторыми вариациями уровней, чтобы отличать даже близкие события. Мы добавим метки на базовой линии для наглядного подчеркивания одномерности временной шкалы. Для каждого события мы добавим текстовую метку с помощью `~.Axes.annotate`, которая смещается в точках от конца линии события. Вот код для создания стволовой диаграммы:

```python
# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```

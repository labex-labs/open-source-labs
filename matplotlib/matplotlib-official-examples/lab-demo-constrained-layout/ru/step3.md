# Создание подграфиков безConstrained Layout

Мы создаем фигуру с 2x2 подграфиками без использования _constrained layout_. В результате метки на осях перекрываются.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```

# Создание подграфиков сConstrained Layout

Мы создаем те же 2x2 подграфики, но на этот раз используем _constrained layout_. Это автоматически настраивает подграфики, чтобы предотвратить перекрытия между объектами осей и метками.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```

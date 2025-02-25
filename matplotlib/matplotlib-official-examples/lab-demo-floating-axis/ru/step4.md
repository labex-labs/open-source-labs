# Создаем основные оси

В этом шаге мы создадим основные оси и настроим вспомогательный объект для сетки. Для создания основных осей мы будем использовать `fig.add_subplot()`.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```

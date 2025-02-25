# Создадим график

Теперь, когда у нас есть наши данные, мы можем создать график. Мы начнем с создания объекта оси с использованием `matplotlib.pyplot.subplots()`. Затем мы построим наш первый набор данных на этом объекте оси и установим цвет метки в красный.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Далее мы создадим второй объект оси, который разделяет ту же ось x, что и первый объект оси, с использованием метода `ax1.twinx()`. Затем мы построим наш второй набор данных на этом новом объекте оси и установим цвет метки в синий.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Наконец, мы настроим макет нашего графика с использованием метода `fig.tight_layout()` и отобразим его с использованием `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```

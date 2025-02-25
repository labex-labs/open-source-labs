# Настроить позицию делений

В этом шаге настройте позицию делений на плавающей оси. Это можно сделать, установив атрибут `tick_out` объекта `major_ticks` в значение `True`.

```python
# Adjust Tick Position
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticks.set_tick_out(True)

plt.show()
```

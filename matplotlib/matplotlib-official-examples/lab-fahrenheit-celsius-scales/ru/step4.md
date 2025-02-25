# Создаем график

Теперь мы создаем график с двумя вертикальными осями с использованием функции `subplots()` из `matplotlib.pyplot`. Также мы связываем событие `ylim_changed` первой оси с функцией `convert_ax_c_to_celsius()`.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```

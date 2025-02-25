# Добавление плавающего оси

Мы определим две функции, которые добавят плавающие оси к нашим графику. Первая функция `add_floating_axis1()` добавляет плавающую ось к графику с меткой `theta = 30`. Вторая функция `add_floating_axis2()` добавляет плавающую ось к графику с меткой `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```

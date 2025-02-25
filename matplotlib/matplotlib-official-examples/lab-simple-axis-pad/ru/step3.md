# Определить функцию добавления плавающей оси

Определите функцию `add_floating_axis`, которая добавляет плавающую ось на график. Эта функция принимает объект `ax1` в качестве аргумента и возвращает объект `axis`.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```

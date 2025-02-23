# Определяем функцию для анимации

Теперь нам нужно определить функцию, которая будет обновлять график для каждого кадра анимации. Эта функция будет получать данные, сгенерированные функцией `data_gen()`, и обновлять график новыми данными. Также мы обновим пределы оси x по мере продвижения анимации.

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```

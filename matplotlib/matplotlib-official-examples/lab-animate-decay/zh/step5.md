# 定义动画函数

现在，我们需要定义一个函数，用于为动画的每一帧更新绘图。这个函数将获取由 `data_gen()` 函数生成的数据，并用新数据更新绘图。随着动画的进行，我们还将更新 x 轴的范围。

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

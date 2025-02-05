# 定义更新函数

我们定义一个函数，用于更新动画每一帧的绘图。该函数有三个输入：`num` 是当前帧数，`walks` 是所有随机游走的列表，`lines` 是绘图中所有线条的列表。对于每条线条和随机游走，我们将线条在当前帧数之前的 x、y 和 z 坐标的数据进行更新。我们分别使用 `line.set_data()` 和 `line.set_3d_properties()` 来更新 x - y 和 z 坐标。

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # 注意：对于三维数据没有.set_data()方法...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```

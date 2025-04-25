# 创建垂直堆叠柱状图

我们将使用`plt.bar`函数创建一个垂直堆叠柱状图，以展示多年来不同自然灾害造成的损失。我们将使用一个 for 循环遍历每一行数据并绘制柱状图。

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```

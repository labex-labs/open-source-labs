# 将渲染器缓冲区提取为 NumPy 数组

保存绘图的第二种选择是将渲染器缓冲区提取为 NumPy 数组。这使我们能够在 CGI 脚本中使用 Matplotlib，而无需将图形写入磁盘。在这个例子中，我们将提取渲染器缓冲区并将其转换为 NumPy 数组。

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```

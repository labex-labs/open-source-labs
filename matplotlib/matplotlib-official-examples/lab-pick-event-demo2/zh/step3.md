# 绘制数据

现在，我们将使用 Matplotlib 的 pyplot 模块绘制 mu 与 sigma 的关系图。我们将使用计算得到的 mu 和 sigma 值创建一个散点图。我们还将通过将 `picker` 参数设置为 True 来为该图添加交互性。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```

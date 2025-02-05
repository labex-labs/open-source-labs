# 将显示对象组合到单个图中

显示对象存储作为参数传递的计算值。这使得可以使用Matplotlib的API轻松地组合可视化效果。在以下示例中，我们将这些显示并排放在一行中。

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```

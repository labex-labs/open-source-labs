# 导入 Matplotlib

在我们开始使用 Matplotlib 为图表添加注释之前，必须先导入该库。在这一步中，我们将导入 Matplotlib 并创建一个简单的图表用于注释。

```python
import matplotlib.pyplot as plt

# 创建一个简单的图表
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```

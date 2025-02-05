# 创建散点图

在这一步中，我们将使用步骤2中的随机数据创建一个散点图。

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```

# 创建图形和子图

我们将使用 `add_gridspec` 方法创建一个包含两个子图的图形。

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```

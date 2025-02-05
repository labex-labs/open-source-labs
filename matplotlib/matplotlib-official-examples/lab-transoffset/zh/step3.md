# 创建散点图

现在我们将使用 `matplotlib.pyplot` 中的 `plot` 函数创建一个散点图。

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# 绘制数据
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```

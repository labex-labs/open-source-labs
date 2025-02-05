# 创建绘图

现在，我们将使用Matplotlib的`subplots`函数来创建绘图。我们将创建两个子图，一个用于绘制垂直线，另一个用于绘制水平线。为了获得更好的可视性，我们将图形大小设置为(12, 6)。

```python
# 创建绘图
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```

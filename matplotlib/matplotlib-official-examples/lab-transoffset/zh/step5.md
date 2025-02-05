# 创建极坐标图

现在我们将使用 `matplotlib.pyplot` 中的 `polar` 函数创建一个极坐标图。

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# 绘制数据
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```

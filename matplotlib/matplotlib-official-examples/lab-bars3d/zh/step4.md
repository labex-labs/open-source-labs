# 自定义条形图

现在我们将自定义条形图。我们将创建一个颜色数组，并使用 `bar()` 方法绘制条形图。我们将把 `zdir` 参数设置为 'y'，以便将条形图投影到y轴平面上。我们还将把 `alpha` 参数设置为0.8，以调整条形的透明度。

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```

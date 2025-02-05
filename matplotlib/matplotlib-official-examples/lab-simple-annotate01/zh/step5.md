# 添加形状注释

我们现在将向绘图添加一个形状注释。以下代码将在第二个数据点周围添加一个矩形。

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("数据点 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="黑色", shrink=0.05))
```

# 添加文本注释

我们现在将向绘图添加一个文本注释。以下代码将在第一个数据点处添加文本“数据点 1”。

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```

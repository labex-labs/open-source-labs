# 添加箭头注释

我们现在将向绘图添加一个箭头注释。以下代码将添加一个从第一个数据点指向第二个数据点的箭头。

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
